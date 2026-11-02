package br.com.financepredict;
import org.junit.jupiter.api.Test;
import org.springframework.web.server.ResponseStatusException;
import java.math.BigDecimal;
import java.util.UUID;
import static org.junit.jupiter.api.Assertions.*;

class BankingControllerTest {
 @Test void handlesDepositsAndWithdrawals() {
   var api=new BankingController();
   UUID id=api.create(new BankingController.CreateAccount("Conta teste")).getBody().id();
   api.deposit(id,new BankingController.AmountRequest(new BigDecimal("150.00")));
   api.withdraw(id,new BankingController.AmountRequest(new BigDecimal("40.00")));
   assertEquals(new BigDecimal("110.00"),api.get(id).balance());
   assertEquals(2,api.transactions(id).size());
 }
 @Test void preventsOverdraftAndMissingAccounts() {
   var api=new BankingController();
   UUID id=api.create(new BankingController.CreateAccount("Teste")).getBody().id();
   assertThrows(ResponseStatusException.class,()->api.withdraw(id,new BankingController.AmountRequest(new BigDecimal("1.00"))));
   assertThrows(ResponseStatusException.class,()->api.get(UUID.randomUUID()));
 }
 @Test void refusesFractionsOfCents() {
   var api=new BankingController();
   UUID id=api.create(new BankingController.CreateAccount("Teste")).getBody().id();
   assertThrows(ResponseStatusException.class,()->api.deposit(id,new BankingController.AmountRequest(new BigDecimal("1.001"))));
 }
}
