package br.com.financepredict;

import jakarta.validation.Valid;
import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;
import java.math.BigDecimal;
import java.time.Instant;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

@RestController
@RequestMapping("/api/v1/accounts")
public class BankingController {
 private final Map<UUID, Account> accounts = new ConcurrentHashMap<>();
 private final Map<UUID, List<Transaction>> history = new ConcurrentHashMap<>();
 public record CreateAccount(@NotBlank String holder) {}
 public record AmountRequest(@NotNull @DecimalMin("0.01") BigDecimal amount) {}
 public record Account(UUID id, String holder, BigDecimal balance) {}
 public record Transaction(UUID id, String type, BigDecimal amount, BigDecimal balanceAfter, Instant date) {}

 @PostMapping
 public ResponseEntity<Account> create(@Valid @RequestBody CreateAccount request) {
   UUID id = UUID.randomUUID();
   Account account = new Account(id,request.holder().trim(),new BigDecimal("0.00"));
   accounts.put(id,account); history.put(id,new ArrayList<>());
   return ResponseEntity.status(HttpStatus.CREATED).body(account);
 }
 @GetMapping("/{id}")
 public Account get(@PathVariable UUID id) {
   Account account=accounts.get(id);
   if(account==null) throw new ResponseStatusException(HttpStatus.NOT_FOUND,"Conta inexistente");
   return account;
 }
 @GetMapping("/{id}/transactions")
 public synchronized List<Transaction> transactions(@PathVariable UUID id) {
   get(id); return List.copyOf(history.get(id));
 }
 @PostMapping("/{id}/deposits")
 public synchronized Account deposit(@PathVariable UUID id,@Valid @RequestBody AmountRequest request) {
   Account old=get(id); BigDecimal amount=currency(request.amount());
   Account next=new Account(id,old.holder(),old.balance().add(amount));
   accounts.put(id,next); log(id,"DEPOSIT",amount,next.balance()); return next;
 }
 @PostMapping("/{id}/withdrawals")
 public synchronized Account withdraw(@PathVariable UUID id,@Valid @RequestBody AmountRequest request) {
   Account old=get(id); BigDecimal amount=currency(request.amount());
   if(old.balance().compareTo(amount)<0) throw new ResponseStatusException(HttpStatus.CONFLICT,"Saldo insuficiente");
   Account next=new Account(id,old.holder(),old.balance().subtract(amount));
   accounts.put(id,next); log(id,"WITHDRAWAL",amount,next.balance()); return next;
 }
 private BigDecimal currency(BigDecimal amount) {
   if(amount.scale()>2) throw new ResponseStatusException(HttpStatus.BAD_REQUEST,"Máximo de duas casas decimais");
   return amount.setScale(2);
 }
 private void log(UUID id,String type,BigDecimal amount,BigDecimal balance) {
   history.get(id).add(new Transaction(UUID.randomUUID(),type,amount,balance,Instant.now()));
 }
}
