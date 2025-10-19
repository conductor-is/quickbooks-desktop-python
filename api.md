# AuthSessions

Types:

```python
from conductor.types import AuthSession
```

Methods:

- <code title="post /auth-sessions">conductor.auth_sessions.<a href="./src/conductor/resources/auth_sessions.py">create</a>(\*\*<a href="src/conductor/types/auth_session_create_params.py">params</a>) -> <a href="./src/conductor/types/auth_session.py">AuthSession</a></code>

# EndUsers

Types:

```python
from conductor.types import (
    EndUser,
    EndUserListResponse,
    EndUserDeleteResponse,
    EndUserPassthroughResponse,
)
```

Methods:

- <code title="post /end-users">conductor.end_users.<a href="./src/conductor/resources/end_users.py">create</a>(\*\*<a href="src/conductor/types/end_user_create_params.py">params</a>) -> <a href="./src/conductor/types/end_user.py">EndUser</a></code>
- <code title="get /end-users/{id}">conductor.end_users.<a href="./src/conductor/resources/end_users.py">retrieve</a>(id) -> <a href="./src/conductor/types/end_user.py">EndUser</a></code>
- <code title="get /end-users">conductor.end_users.<a href="./src/conductor/resources/end_users.py">list</a>() -> <a href="./src/conductor/types/end_user_list_response.py">EndUserListResponse</a></code>
- <code title="delete /end-users/{id}">conductor.end_users.<a href="./src/conductor/resources/end_users.py">delete</a>(id) -> <a href="./src/conductor/types/end_user_delete_response.py">EndUserDeleteResponse</a></code>
- <code title="post /end-users/{id}/passthrough/{integrationSlug}">conductor.end_users.<a href="./src/conductor/resources/end_users.py">passthrough</a>(integration_slug, \*, id, \*\*<a href="src/conductor/types/end_user_passthrough_params.py">params</a>) -> <a href="./src/conductor/types/end_user_passthrough_response.py">EndUserPassthroughResponse</a></code>

# Qbd

Types:

```python
from conductor.types import QbdHealthCheckResponse
```

Methods:

- <code title="get /quickbooks-desktop/health-check">conductor.qbd.<a href="./src/conductor/resources/qbd/qbd.py">health_check</a>() -> <a href="./src/conductor/types/qbd_health_check_response.py">QbdHealthCheckResponse</a></code>

## AccountTaxLines

Types:

```python
from conductor.types.qbd import AccountTaxLine, AccountTaxLineListResponse
```

Methods:

- <code title="get /quickbooks-desktop/account-tax-lines">conductor.qbd.account_tax_lines.<a href="./src/conductor/resources/qbd/account_tax_lines.py">list</a>() -> <a href="./src/conductor/types/qbd/account_tax_line_list_response.py">AccountTaxLineListResponse</a></code>

## Accounts

Types:

```python
from conductor.types.qbd import Account, AccountListResponse
```

Methods:

- <code title="post /quickbooks-desktop/accounts">conductor.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">create</a>(\*\*<a href="src/conductor/types/qbd/account_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/account.py">Account</a></code>
- <code title="get /quickbooks-desktop/accounts/{id}">conductor.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/account.py">Account</a></code>
- <code title="post /quickbooks-desktop/accounts/{id}">conductor.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/account_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/account.py">Account</a></code>
- <code title="get /quickbooks-desktop/accounts">conductor.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">list</a>(\*\*<a href="src/conductor/types/qbd/account_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/account_list_response.py">AccountListResponse</a></code>

## BillCheckPayments

Types:

```python
from conductor.types.qbd import BillCheckPayment, BillCheckPaymentDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/bill-check-payments">conductor.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">create</a>(\*\*<a href="src/conductor/types/qbd/bill_check_payment_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_check_payment.py">BillCheckPayment</a></code>
- <code title="get /quickbooks-desktop/bill-check-payments/{id}">conductor.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/bill_check_payment.py">BillCheckPayment</a></code>
- <code title="post /quickbooks-desktop/bill-check-payments/{id}">conductor.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/bill_check_payment_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_check_payment.py">BillCheckPayment</a></code>
- <code title="get /quickbooks-desktop/bill-check-payments">conductor.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">list</a>(\*\*<a href="src/conductor/types/qbd/bill_check_payment_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_check_payment.py">SyncCursorPage[BillCheckPayment]</a></code>
- <code title="delete /quickbooks-desktop/bill-check-payments/{id}">conductor.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/bill_check_payment_delete_response.py">BillCheckPaymentDeleteResponse</a></code>

## BillCreditCardPayments

Types:

```python
from conductor.types.qbd import BillCreditCardPayment, BillCreditCardPaymentDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/bill-credit-card-payments">conductor.qbd.bill_credit_card_payments.<a href="./src/conductor/resources/qbd/bill_credit_card_payments.py">create</a>(\*\*<a href="src/conductor/types/qbd/bill_credit_card_payment_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_credit_card_payment.py">BillCreditCardPayment</a></code>
- <code title="get /quickbooks-desktop/bill-credit-card-payments/{id}">conductor.qbd.bill_credit_card_payments.<a href="./src/conductor/resources/qbd/bill_credit_card_payments.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/bill_credit_card_payment.py">BillCreditCardPayment</a></code>
- <code title="get /quickbooks-desktop/bill-credit-card-payments">conductor.qbd.bill_credit_card_payments.<a href="./src/conductor/resources/qbd/bill_credit_card_payments.py">list</a>(\*\*<a href="src/conductor/types/qbd/bill_credit_card_payment_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_credit_card_payment.py">SyncCursorPage[BillCreditCardPayment]</a></code>
- <code title="delete /quickbooks-desktop/bill-credit-card-payments/{id}">conductor.qbd.bill_credit_card_payments.<a href="./src/conductor/resources/qbd/bill_credit_card_payments.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/bill_credit_card_payment_delete_response.py">BillCreditCardPaymentDeleteResponse</a></code>

## Bills

Types:

```python
from conductor.types.qbd import Bill, BillDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/bills">conductor.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">create</a>(\*\*<a href="src/conductor/types/qbd/bill_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill.py">Bill</a></code>
- <code title="get /quickbooks-desktop/bills/{id}">conductor.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/bill.py">Bill</a></code>
- <code title="post /quickbooks-desktop/bills/{id}">conductor.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/bill_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill.py">Bill</a></code>
- <code title="get /quickbooks-desktop/bills">conductor.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">list</a>(\*\*<a href="src/conductor/types/qbd/bill_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill.py">SyncCursorPage[Bill]</a></code>
- <code title="delete /quickbooks-desktop/bills/{id}">conductor.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/bill_delete_response.py">BillDeleteResponse</a></code>

## BuildAssemblies

Types:

```python
from conductor.types.qbd import BuildAssembly, BuildAssemblyDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/build-assemblies">conductor.qbd.build_assemblies.<a href="./src/conductor/resources/qbd/build_assemblies.py">create</a>(\*\*<a href="src/conductor/types/qbd/build_assembly_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/build_assembly.py">BuildAssembly</a></code>
- <code title="get /quickbooks-desktop/build-assemblies/{id}">conductor.qbd.build_assemblies.<a href="./src/conductor/resources/qbd/build_assemblies.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/build_assembly.py">BuildAssembly</a></code>
- <code title="post /quickbooks-desktop/build-assemblies/{id}">conductor.qbd.build_assemblies.<a href="./src/conductor/resources/qbd/build_assemblies.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/build_assembly_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/build_assembly.py">BuildAssembly</a></code>
- <code title="get /quickbooks-desktop/build-assemblies">conductor.qbd.build_assemblies.<a href="./src/conductor/resources/qbd/build_assemblies.py">list</a>(\*\*<a href="src/conductor/types/qbd/build_assembly_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/build_assembly.py">SyncCursorPage[BuildAssembly]</a></code>
- <code title="delete /quickbooks-desktop/build-assemblies/{id}">conductor.qbd.build_assemblies.<a href="./src/conductor/resources/qbd/build_assemblies.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/build_assembly_delete_response.py">BuildAssemblyDeleteResponse</a></code>

## Checks

Types:

```python
from conductor.types.qbd import Check, CheckDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/checks">conductor.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">create</a>(\*\*<a href="src/conductor/types/qbd/check_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/check.py">Check</a></code>
- <code title="get /quickbooks-desktop/checks/{id}">conductor.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/check.py">Check</a></code>
- <code title="post /quickbooks-desktop/checks/{id}">conductor.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/check_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/check.py">Check</a></code>
- <code title="get /quickbooks-desktop/checks">conductor.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">list</a>(\*\*<a href="src/conductor/types/qbd/check_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/check.py">SyncCursorPage[Check]</a></code>
- <code title="delete /quickbooks-desktop/checks/{id}">conductor.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/check_delete_response.py">CheckDeleteResponse</a></code>

## Classes

Types:

```python
from conductor.types.qbd import Class, ClassListResponse
```

Methods:

- <code title="post /quickbooks-desktop/classes">conductor.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">create</a>(\*\*<a href="src/conductor/types/qbd/class_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/class_.py">Class</a></code>
- <code title="get /quickbooks-desktop/classes/{id}">conductor.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/class_.py">Class</a></code>
- <code title="post /quickbooks-desktop/classes/{id}">conductor.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/class_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/class_.py">Class</a></code>
- <code title="get /quickbooks-desktop/classes">conductor.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">list</a>(\*\*<a href="src/conductor/types/qbd/class_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/class_list_response.py">ClassListResponse</a></code>

## Company

Types:

```python
from conductor.types.qbd import Company
```

Methods:

- <code title="get /quickbooks-desktop/company">conductor.qbd.company.<a href="./src/conductor/resources/qbd/company.py">retrieve</a>() -> <a href="./src/conductor/types/qbd/company.py">Company</a></code>

## CreditCardCharges

Types:

```python
from conductor.types.qbd import CreditCardCharge, CreditCardChargeDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/credit-card-charges">conductor.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">create</a>(\*\*<a href="src/conductor/types/qbd/credit_card_charge_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_charge.py">CreditCardCharge</a></code>
- <code title="get /quickbooks-desktop/credit-card-charges/{id}">conductor.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/credit_card_charge.py">CreditCardCharge</a></code>
- <code title="post /quickbooks-desktop/credit-card-charges/{id}">conductor.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/credit_card_charge_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_charge.py">CreditCardCharge</a></code>
- <code title="get /quickbooks-desktop/credit-card-charges">conductor.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">list</a>(\*\*<a href="src/conductor/types/qbd/credit_card_charge_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_charge.py">SyncCursorPage[CreditCardCharge]</a></code>
- <code title="delete /quickbooks-desktop/credit-card-charges/{id}">conductor.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/credit_card_charge_delete_response.py">CreditCardChargeDeleteResponse</a></code>

## CreditCardCredits

Types:

```python
from conductor.types.qbd import CreditCardCredit, CreditCardCreditDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/credit-card-credits">conductor.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">create</a>(\*\*<a href="src/conductor/types/qbd/credit_card_credit_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_credit.py">CreditCardCredit</a></code>
- <code title="get /quickbooks-desktop/credit-card-credits/{id}">conductor.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/credit_card_credit.py">CreditCardCredit</a></code>
- <code title="post /quickbooks-desktop/credit-card-credits/{id}">conductor.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/credit_card_credit_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_credit.py">CreditCardCredit</a></code>
- <code title="get /quickbooks-desktop/credit-card-credits">conductor.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">list</a>(\*\*<a href="src/conductor/types/qbd/credit_card_credit_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_credit.py">SyncCursorPage[CreditCardCredit]</a></code>
- <code title="delete /quickbooks-desktop/credit-card-credits/{id}">conductor.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/credit_card_credit_delete_response.py">CreditCardCreditDeleteResponse</a></code>

## CreditCardRefunds

Types:

```python
from conductor.types.qbd import CreditCardRefund, CreditCardRefundDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/credit-card-refunds">conductor.qbd.credit_card_refunds.<a href="./src/conductor/resources/qbd/credit_card_refunds.py">create</a>(\*\*<a href="src/conductor/types/qbd/credit_card_refund_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_refund.py">CreditCardRefund</a></code>
- <code title="get /quickbooks-desktop/credit-card-refunds/{id}">conductor.qbd.credit_card_refunds.<a href="./src/conductor/resources/qbd/credit_card_refunds.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/credit_card_refund.py">CreditCardRefund</a></code>
- <code title="get /quickbooks-desktop/credit-card-refunds">conductor.qbd.credit_card_refunds.<a href="./src/conductor/resources/qbd/credit_card_refunds.py">list</a>(\*\*<a href="src/conductor/types/qbd/credit_card_refund_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_refund.py">SyncCursorPage[CreditCardRefund]</a></code>
- <code title="delete /quickbooks-desktop/credit-card-refunds/{id}">conductor.qbd.credit_card_refunds.<a href="./src/conductor/resources/qbd/credit_card_refunds.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/credit_card_refund_delete_response.py">CreditCardRefundDeleteResponse</a></code>

## CreditMemos

Types:

```python
from conductor.types.qbd import CreditMemo, CreditMemoDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/credit-memos">conductor.qbd.credit_memos.<a href="./src/conductor/resources/qbd/credit_memos.py">create</a>(\*\*<a href="src/conductor/types/qbd/credit_memo_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_memo.py">CreditMemo</a></code>
- <code title="get /quickbooks-desktop/credit-memos/{id}">conductor.qbd.credit_memos.<a href="./src/conductor/resources/qbd/credit_memos.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/credit_memo.py">CreditMemo</a></code>
- <code title="post /quickbooks-desktop/credit-memos/{id}">conductor.qbd.credit_memos.<a href="./src/conductor/resources/qbd/credit_memos.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/credit_memo_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_memo.py">CreditMemo</a></code>
- <code title="get /quickbooks-desktop/credit-memos">conductor.qbd.credit_memos.<a href="./src/conductor/resources/qbd/credit_memos.py">list</a>(\*\*<a href="src/conductor/types/qbd/credit_memo_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_memo.py">SyncCursorPage[CreditMemo]</a></code>
- <code title="delete /quickbooks-desktop/credit-memos/{id}">conductor.qbd.credit_memos.<a href="./src/conductor/resources/qbd/credit_memos.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/credit_memo_delete_response.py">CreditMemoDeleteResponse</a></code>

## Currencies

Types:

```python
from conductor.types.qbd import Currency, CurrencyListResponse
```

Methods:

- <code title="post /quickbooks-desktop/currencies">conductor.qbd.currencies.<a href="./src/conductor/resources/qbd/currencies.py">create</a>(\*\*<a href="src/conductor/types/qbd/currency_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/currency.py">Currency</a></code>
- <code title="get /quickbooks-desktop/currencies/{id}">conductor.qbd.currencies.<a href="./src/conductor/resources/qbd/currencies.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/currency.py">Currency</a></code>
- <code title="post /quickbooks-desktop/currencies/{id}">conductor.qbd.currencies.<a href="./src/conductor/resources/qbd/currencies.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/currency_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/currency.py">Currency</a></code>
- <code title="get /quickbooks-desktop/currencies">conductor.qbd.currencies.<a href="./src/conductor/resources/qbd/currencies.py">list</a>(\*\*<a href="src/conductor/types/qbd/currency_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/currency_list_response.py">CurrencyListResponse</a></code>

## CustomerTypes

Types:

```python
from conductor.types.qbd import CustomerType, CustomerTypeListResponse
```

Methods:

- <code title="post /quickbooks-desktop/customer-types">conductor.qbd.customer_types.<a href="./src/conductor/resources/qbd/customer_types.py">create</a>(\*\*<a href="src/conductor/types/qbd/customer_type_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/customer_type.py">CustomerType</a></code>
- <code title="get /quickbooks-desktop/customer-types/{id}">conductor.qbd.customer_types.<a href="./src/conductor/resources/qbd/customer_types.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/customer_type.py">CustomerType</a></code>
- <code title="get /quickbooks-desktop/customer-types">conductor.qbd.customer_types.<a href="./src/conductor/resources/qbd/customer_types.py">list</a>(\*\*<a href="src/conductor/types/qbd/customer_type_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/customer_type_list_response.py">CustomerTypeListResponse</a></code>

## Customers

Types:

```python
from conductor.types.qbd import Customer
```

Methods:

- <code title="post /quickbooks-desktop/customers">conductor.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">create</a>(\*\*<a href="src/conductor/types/qbd/customer_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/customer.py">Customer</a></code>
- <code title="get /quickbooks-desktop/customers/{id}">conductor.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/customer.py">Customer</a></code>
- <code title="post /quickbooks-desktop/customers/{id}">conductor.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/customer_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/customer.py">Customer</a></code>
- <code title="get /quickbooks-desktop/customers">conductor.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">list</a>(\*\*<a href="src/conductor/types/qbd/customer_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/customer.py">SyncCursorPage[Customer]</a></code>

## DateDrivenTerms

Types:

```python
from conductor.types.qbd import DateDrivenTerm, DateDrivenTermListResponse
```

Methods:

- <code title="post /quickbooks-desktop/date-driven-terms">conductor.qbd.date_driven_terms.<a href="./src/conductor/resources/qbd/date_driven_terms.py">create</a>(\*\*<a href="src/conductor/types/qbd/date_driven_term_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/date_driven_term.py">DateDrivenTerm</a></code>
- <code title="get /quickbooks-desktop/date-driven-terms/{id}">conductor.qbd.date_driven_terms.<a href="./src/conductor/resources/qbd/date_driven_terms.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/date_driven_term.py">DateDrivenTerm</a></code>
- <code title="get /quickbooks-desktop/date-driven-terms">conductor.qbd.date_driven_terms.<a href="./src/conductor/resources/qbd/date_driven_terms.py">list</a>(\*\*<a href="src/conductor/types/qbd/date_driven_term_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/date_driven_term_list_response.py">DateDrivenTermListResponse</a></code>

## DeletedListObjects

Types:

```python
from conductor.types.qbd import DeletedListObject, DeletedListObjectListResponse
```

Methods:

- <code title="get /quickbooks-desktop/deleted-list-objects">conductor.qbd.deleted_list_objects.<a href="./src/conductor/resources/qbd/deleted_list_objects.py">list</a>(\*\*<a href="src/conductor/types/qbd/deleted_list_object_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/deleted_list_object_list_response.py">DeletedListObjectListResponse</a></code>

## DeletedTransactions

Types:

```python
from conductor.types.qbd import DeletedTransaction, DeletedTransactionListResponse
```

Methods:

- <code title="get /quickbooks-desktop/deleted-transactions">conductor.qbd.deleted_transactions.<a href="./src/conductor/resources/qbd/deleted_transactions.py">list</a>(\*\*<a href="src/conductor/types/qbd/deleted_transaction_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/deleted_transaction_list_response.py">DeletedTransactionListResponse</a></code>

## DiscountItems

Types:

```python
from conductor.types.qbd import DiscountItem
```

Methods:

- <code title="post /quickbooks-desktop/discount-items">conductor.qbd.discount_items.<a href="./src/conductor/resources/qbd/discount_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/discount_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/discount_item.py">DiscountItem</a></code>
- <code title="get /quickbooks-desktop/discount-items/{id}">conductor.qbd.discount_items.<a href="./src/conductor/resources/qbd/discount_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/discount_item.py">DiscountItem</a></code>
- <code title="post /quickbooks-desktop/discount-items/{id}">conductor.qbd.discount_items.<a href="./src/conductor/resources/qbd/discount_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/discount_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/discount_item.py">DiscountItem</a></code>
- <code title="get /quickbooks-desktop/discount-items">conductor.qbd.discount_items.<a href="./src/conductor/resources/qbd/discount_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/discount_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/discount_item.py">SyncCursorPage[DiscountItem]</a></code>

## Employees

Types:

```python
from conductor.types.qbd import Employee, EmployeeListResponse
```

Methods:

- <code title="post /quickbooks-desktop/employees">conductor.qbd.employees.<a href="./src/conductor/resources/qbd/employees.py">create</a>(\*\*<a href="src/conductor/types/qbd/employee_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/employee.py">Employee</a></code>
- <code title="get /quickbooks-desktop/employees/{id}">conductor.qbd.employees.<a href="./src/conductor/resources/qbd/employees.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/employee.py">Employee</a></code>
- <code title="post /quickbooks-desktop/employees/{id}">conductor.qbd.employees.<a href="./src/conductor/resources/qbd/employees.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/employee_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/employee.py">Employee</a></code>
- <code title="get /quickbooks-desktop/employees">conductor.qbd.employees.<a href="./src/conductor/resources/qbd/employees.py">list</a>(\*\*<a href="src/conductor/types/qbd/employee_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/employee_list_response.py">EmployeeListResponse</a></code>

## Estimates

Types:

```python
from conductor.types.qbd import Estimate, EstimateDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/estimates">conductor.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">create</a>(\*\*<a href="src/conductor/types/qbd/estimate_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/estimate.py">Estimate</a></code>
- <code title="get /quickbooks-desktop/estimates/{id}">conductor.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/estimate.py">Estimate</a></code>
- <code title="post /quickbooks-desktop/estimates/{id}">conductor.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/estimate_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/estimate.py">Estimate</a></code>
- <code title="get /quickbooks-desktop/estimates">conductor.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">list</a>(\*\*<a href="src/conductor/types/qbd/estimate_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/estimate.py">SyncCursorPage[Estimate]</a></code>
- <code title="delete /quickbooks-desktop/estimates/{id}">conductor.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/estimate_delete_response.py">EstimateDeleteResponse</a></code>

## InventoryAdjustments

Types:

```python
from conductor.types.qbd import (
    InventoryAdjustment,
    InventoryAdjustmentListResponse,
    InventoryAdjustmentDeleteResponse,
)
```

Methods:

- <code title="post /quickbooks-desktop/inventory-adjustments">conductor.qbd.inventory_adjustments.<a href="./src/conductor/resources/qbd/inventory_adjustments.py">create</a>(\*\*<a href="src/conductor/types/qbd/inventory_adjustment_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_adjustment.py">InventoryAdjustment</a></code>
- <code title="get /quickbooks-desktop/inventory-adjustments/{id}">conductor.qbd.inventory_adjustments.<a href="./src/conductor/resources/qbd/inventory_adjustments.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/inventory_adjustment.py">InventoryAdjustment</a></code>
- <code title="post /quickbooks-desktop/inventory-adjustments/{id}">conductor.qbd.inventory_adjustments.<a href="./src/conductor/resources/qbd/inventory_adjustments.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/inventory_adjustment_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_adjustment.py">InventoryAdjustment</a></code>
- <code title="get /quickbooks-desktop/inventory-adjustments">conductor.qbd.inventory_adjustments.<a href="./src/conductor/resources/qbd/inventory_adjustments.py">list</a>(\*\*<a href="src/conductor/types/qbd/inventory_adjustment_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_adjustment_list_response.py">InventoryAdjustmentListResponse</a></code>
- <code title="delete /quickbooks-desktop/inventory-adjustments/{id}">conductor.qbd.inventory_adjustments.<a href="./src/conductor/resources/qbd/inventory_adjustments.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/inventory_adjustment_delete_response.py">InventoryAdjustmentDeleteResponse</a></code>

## InventoryAssemblyItems

Types:

```python
from conductor.types.qbd import InventoryAssemblyItem
```

Methods:

- <code title="post /quickbooks-desktop/inventory-assembly-items">conductor.qbd.inventory_assembly_items.<a href="./src/conductor/resources/qbd/inventory_assembly_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/inventory_assembly_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_assembly_item.py">InventoryAssemblyItem</a></code>
- <code title="get /quickbooks-desktop/inventory-assembly-items/{id}">conductor.qbd.inventory_assembly_items.<a href="./src/conductor/resources/qbd/inventory_assembly_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/inventory_assembly_item.py">InventoryAssemblyItem</a></code>
- <code title="post /quickbooks-desktop/inventory-assembly-items/{id}">conductor.qbd.inventory_assembly_items.<a href="./src/conductor/resources/qbd/inventory_assembly_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/inventory_assembly_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_assembly_item.py">InventoryAssemblyItem</a></code>
- <code title="get /quickbooks-desktop/inventory-assembly-items">conductor.qbd.inventory_assembly_items.<a href="./src/conductor/resources/qbd/inventory_assembly_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/inventory_assembly_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_assembly_item.py">SyncCursorPage[InventoryAssemblyItem]</a></code>

## InventoryItems

Types:

```python
from conductor.types.qbd import InventoryItem
```

Methods:

- <code title="post /quickbooks-desktop/inventory-items">conductor.qbd.inventory_items.<a href="./src/conductor/resources/qbd/inventory_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/inventory_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_item.py">InventoryItem</a></code>
- <code title="get /quickbooks-desktop/inventory-items/{id}">conductor.qbd.inventory_items.<a href="./src/conductor/resources/qbd/inventory_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/inventory_item.py">InventoryItem</a></code>
- <code title="post /quickbooks-desktop/inventory-items/{id}">conductor.qbd.inventory_items.<a href="./src/conductor/resources/qbd/inventory_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/inventory_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_item.py">InventoryItem</a></code>
- <code title="get /quickbooks-desktop/inventory-items">conductor.qbd.inventory_items.<a href="./src/conductor/resources/qbd/inventory_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/inventory_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_item.py">SyncCursorPage[InventoryItem]</a></code>

## InventorySites

Types:

```python
from conductor.types.qbd import InventorySite, InventorySiteListResponse
```

Methods:

- <code title="post /quickbooks-desktop/inventory-sites">conductor.qbd.inventory_sites.<a href="./src/conductor/resources/qbd/inventory_sites.py">create</a>(\*\*<a href="src/conductor/types/qbd/inventory_site_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_site.py">InventorySite</a></code>
- <code title="get /quickbooks-desktop/inventory-sites/{id}">conductor.qbd.inventory_sites.<a href="./src/conductor/resources/qbd/inventory_sites.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/inventory_site.py">InventorySite</a></code>
- <code title="post /quickbooks-desktop/inventory-sites/{id}">conductor.qbd.inventory_sites.<a href="./src/conductor/resources/qbd/inventory_sites.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/inventory_site_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_site.py">InventorySite</a></code>
- <code title="get /quickbooks-desktop/inventory-sites">conductor.qbd.inventory_sites.<a href="./src/conductor/resources/qbd/inventory_sites.py">list</a>(\*\*<a href="src/conductor/types/qbd/inventory_site_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_site_list_response.py">InventorySiteListResponse</a></code>

## Invoices

Types:

```python
from conductor.types.qbd import Invoice, InvoiceDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/invoices">conductor.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">create</a>(\*\*<a href="src/conductor/types/qbd/invoice_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/invoice.py">Invoice</a></code>
- <code title="get /quickbooks-desktop/invoices/{id}">conductor.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/invoice.py">Invoice</a></code>
- <code title="post /quickbooks-desktop/invoices/{id}">conductor.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/invoice_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/invoice.py">Invoice</a></code>
- <code title="get /quickbooks-desktop/invoices">conductor.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">list</a>(\*\*<a href="src/conductor/types/qbd/invoice_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/invoice.py">SyncCursorPage[Invoice]</a></code>
- <code title="delete /quickbooks-desktop/invoices/{id}">conductor.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/invoice_delete_response.py">InvoiceDeleteResponse</a></code>

## ItemGroups

Types:

```python
from conductor.types.qbd import ItemGroup
```

Methods:

- <code title="post /quickbooks-desktop/item-groups">conductor.qbd.item_groups.<a href="./src/conductor/resources/qbd/item_groups.py">create</a>(\*\*<a href="src/conductor/types/qbd/item_group_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/item_group.py">ItemGroup</a></code>
- <code title="get /quickbooks-desktop/item-groups/{id}">conductor.qbd.item_groups.<a href="./src/conductor/resources/qbd/item_groups.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/item_group.py">ItemGroup</a></code>
- <code title="post /quickbooks-desktop/item-groups/{id}">conductor.qbd.item_groups.<a href="./src/conductor/resources/qbd/item_groups.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/item_group_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/item_group.py">ItemGroup</a></code>
- <code title="get /quickbooks-desktop/item-groups">conductor.qbd.item_groups.<a href="./src/conductor/resources/qbd/item_groups.py">list</a>(\*\*<a href="src/conductor/types/qbd/item_group_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/item_group.py">SyncCursorPage[ItemGroup]</a></code>

## ItemReceipts

Types:

```python
from conductor.types.qbd import ItemReceipt, ItemReceiptDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/item-receipts">conductor.qbd.item_receipts.<a href="./src/conductor/resources/qbd/item_receipts.py">create</a>(\*\*<a href="src/conductor/types/qbd/item_receipt_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/item_receipt.py">ItemReceipt</a></code>
- <code title="get /quickbooks-desktop/item-receipts/{id}">conductor.qbd.item_receipts.<a href="./src/conductor/resources/qbd/item_receipts.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/item_receipt.py">ItemReceipt</a></code>
- <code title="post /quickbooks-desktop/item-receipts/{id}">conductor.qbd.item_receipts.<a href="./src/conductor/resources/qbd/item_receipts.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/item_receipt_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/item_receipt.py">ItemReceipt</a></code>
- <code title="get /quickbooks-desktop/item-receipts">conductor.qbd.item_receipts.<a href="./src/conductor/resources/qbd/item_receipts.py">list</a>(\*\*<a href="src/conductor/types/qbd/item_receipt_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/item_receipt.py">SyncCursorPage[ItemReceipt]</a></code>
- <code title="delete /quickbooks-desktop/item-receipts/{id}">conductor.qbd.item_receipts.<a href="./src/conductor/resources/qbd/item_receipts.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/item_receipt_delete_response.py">ItemReceiptDeleteResponse</a></code>

## ItemSites

Types:

```python
from conductor.types.qbd import ItemSite
```

Methods:

- <code title="get /quickbooks-desktop/item-sites/{id}">conductor.qbd.item_sites.<a href="./src/conductor/resources/qbd/item_sites.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/item_site.py">ItemSite</a></code>
- <code title="get /quickbooks-desktop/item-sites">conductor.qbd.item_sites.<a href="./src/conductor/resources/qbd/item_sites.py">list</a>(\*\*<a href="src/conductor/types/qbd/item_site_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/item_site.py">SyncCursorPage[ItemSite]</a></code>

## JournalEntries

Types:

```python
from conductor.types.qbd import JournalEntry, JournalEntryDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/journal-entries">conductor.qbd.journal_entries.<a href="./src/conductor/resources/qbd/journal_entries.py">create</a>(\*\*<a href="src/conductor/types/qbd/journal_entry_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/journal_entry.py">JournalEntry</a></code>
- <code title="get /quickbooks-desktop/journal-entries/{id}">conductor.qbd.journal_entries.<a href="./src/conductor/resources/qbd/journal_entries.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/journal_entry.py">JournalEntry</a></code>
- <code title="post /quickbooks-desktop/journal-entries/{id}">conductor.qbd.journal_entries.<a href="./src/conductor/resources/qbd/journal_entries.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/journal_entry_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/journal_entry.py">JournalEntry</a></code>
- <code title="get /quickbooks-desktop/journal-entries">conductor.qbd.journal_entries.<a href="./src/conductor/resources/qbd/journal_entries.py">list</a>(\*\*<a href="src/conductor/types/qbd/journal_entry_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/journal_entry.py">SyncCursorPage[JournalEntry]</a></code>
- <code title="delete /quickbooks-desktop/journal-entries/{id}">conductor.qbd.journal_entries.<a href="./src/conductor/resources/qbd/journal_entries.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/journal_entry_delete_response.py">JournalEntryDeleteResponse</a></code>

## NonInventoryItems

Types:

```python
from conductor.types.qbd import NonInventoryItem
```

Methods:

- <code title="post /quickbooks-desktop/non-inventory-items">conductor.qbd.non_inventory_items.<a href="./src/conductor/resources/qbd/non_inventory_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/non_inventory_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/non_inventory_item.py">NonInventoryItem</a></code>
- <code title="get /quickbooks-desktop/non-inventory-items/{id}">conductor.qbd.non_inventory_items.<a href="./src/conductor/resources/qbd/non_inventory_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/non_inventory_item.py">NonInventoryItem</a></code>
- <code title="post /quickbooks-desktop/non-inventory-items/{id}">conductor.qbd.non_inventory_items.<a href="./src/conductor/resources/qbd/non_inventory_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/non_inventory_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/non_inventory_item.py">NonInventoryItem</a></code>
- <code title="get /quickbooks-desktop/non-inventory-items">conductor.qbd.non_inventory_items.<a href="./src/conductor/resources/qbd/non_inventory_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/non_inventory_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/non_inventory_item.py">SyncCursorPage[NonInventoryItem]</a></code>

## OtherChargeItems

Types:

```python
from conductor.types.qbd import OtherChargeItem
```

Methods:

- <code title="post /quickbooks-desktop/other-charge-items">conductor.qbd.other_charge_items.<a href="./src/conductor/resources/qbd/other_charge_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/other_charge_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/other_charge_item.py">OtherChargeItem</a></code>
- <code title="get /quickbooks-desktop/other-charge-items/{id}">conductor.qbd.other_charge_items.<a href="./src/conductor/resources/qbd/other_charge_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/other_charge_item.py">OtherChargeItem</a></code>
- <code title="post /quickbooks-desktop/other-charge-items/{id}">conductor.qbd.other_charge_items.<a href="./src/conductor/resources/qbd/other_charge_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/other_charge_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/other_charge_item.py">OtherChargeItem</a></code>
- <code title="get /quickbooks-desktop/other-charge-items">conductor.qbd.other_charge_items.<a href="./src/conductor/resources/qbd/other_charge_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/other_charge_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/other_charge_item.py">SyncCursorPage[OtherChargeItem]</a></code>

## OtherNames

Types:

```python
from conductor.types.qbd import OtherName, OtherNameListResponse
```

Methods:

- <code title="post /quickbooks-desktop/other-names">conductor.qbd.other_names.<a href="./src/conductor/resources/qbd/other_names.py">create</a>(\*\*<a href="src/conductor/types/qbd/other_name_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/other_name.py">OtherName</a></code>
- <code title="get /quickbooks-desktop/other-names/{id}">conductor.qbd.other_names.<a href="./src/conductor/resources/qbd/other_names.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/other_name.py">OtherName</a></code>
- <code title="post /quickbooks-desktop/other-names/{id}">conductor.qbd.other_names.<a href="./src/conductor/resources/qbd/other_names.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/other_name_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/other_name.py">OtherName</a></code>
- <code title="get /quickbooks-desktop/other-names">conductor.qbd.other_names.<a href="./src/conductor/resources/qbd/other_names.py">list</a>(\*\*<a href="src/conductor/types/qbd/other_name_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/other_name_list_response.py">OtherNameListResponse</a></code>

## PaymentMethods

Types:

```python
from conductor.types.qbd import PaymentMethod, PaymentMethodListResponse
```

Methods:

- <code title="post /quickbooks-desktop/payment-methods">conductor.qbd.payment_methods.<a href="./src/conductor/resources/qbd/payment_methods.py">create</a>(\*\*<a href="src/conductor/types/qbd/payment_method_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/payment_method.py">PaymentMethod</a></code>
- <code title="get /quickbooks-desktop/payment-methods/{id}">conductor.qbd.payment_methods.<a href="./src/conductor/resources/qbd/payment_methods.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/payment_method.py">PaymentMethod</a></code>
- <code title="get /quickbooks-desktop/payment-methods">conductor.qbd.payment_methods.<a href="./src/conductor/resources/qbd/payment_methods.py">list</a>(\*\*<a href="src/conductor/types/qbd/payment_method_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/payment_method_list_response.py">PaymentMethodListResponse</a></code>

## PayrollWageItems

Types:

```python
from conductor.types.qbd import PayrollWageItem
```

Methods:

- <code title="post /quickbooks-desktop/payroll-wage-items">conductor.qbd.payroll_wage_items.<a href="./src/conductor/resources/qbd/payroll_wage_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/payroll_wage_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/payroll_wage_item.py">PayrollWageItem</a></code>
- <code title="get /quickbooks-desktop/payroll-wage-items/{id}">conductor.qbd.payroll_wage_items.<a href="./src/conductor/resources/qbd/payroll_wage_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/payroll_wage_item.py">PayrollWageItem</a></code>
- <code title="get /quickbooks-desktop/payroll-wage-items">conductor.qbd.payroll_wage_items.<a href="./src/conductor/resources/qbd/payroll_wage_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/payroll_wage_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/payroll_wage_item.py">SyncCursorPage[PayrollWageItem]</a></code>

## Preferences

Types:

```python
from conductor.types.qbd import Preferences
```

Methods:

- <code title="get /quickbooks-desktop/preferences">conductor.qbd.preferences.<a href="./src/conductor/resources/qbd/preferences.py">retrieve</a>() -> <a href="./src/conductor/types/qbd/preferences.py">Preferences</a></code>

## PriceLevels

Types:

```python
from conductor.types.qbd import PriceLevel, PriceLevelListResponse
```

Methods:

- <code title="post /quickbooks-desktop/price-levels">conductor.qbd.price_levels.<a href="./src/conductor/resources/qbd/price_levels.py">create</a>(\*\*<a href="src/conductor/types/qbd/price_level_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/price_level.py">PriceLevel</a></code>
- <code title="get /quickbooks-desktop/price-levels/{id}">conductor.qbd.price_levels.<a href="./src/conductor/resources/qbd/price_levels.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/price_level.py">PriceLevel</a></code>
- <code title="post /quickbooks-desktop/price-levels/{id}">conductor.qbd.price_levels.<a href="./src/conductor/resources/qbd/price_levels.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/price_level_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/price_level.py">PriceLevel</a></code>
- <code title="get /quickbooks-desktop/price-levels">conductor.qbd.price_levels.<a href="./src/conductor/resources/qbd/price_levels.py">list</a>(\*\*<a href="src/conductor/types/qbd/price_level_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/price_level_list_response.py">PriceLevelListResponse</a></code>

## PurchaseOrders

Types:

```python
from conductor.types.qbd import PurchaseOrder, PurchaseOrderDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/purchase-orders">conductor.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">create</a>(\*\*<a href="src/conductor/types/qbd/purchase_order_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/purchase_order.py">PurchaseOrder</a></code>
- <code title="get /quickbooks-desktop/purchase-orders/{id}">conductor.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/purchase_order.py">PurchaseOrder</a></code>
- <code title="post /quickbooks-desktop/purchase-orders/{id}">conductor.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/purchase_order_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/purchase_order.py">PurchaseOrder</a></code>
- <code title="get /quickbooks-desktop/purchase-orders">conductor.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">list</a>(\*\*<a href="src/conductor/types/qbd/purchase_order_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/purchase_order.py">SyncCursorPage[PurchaseOrder]</a></code>
- <code title="delete /quickbooks-desktop/purchase-orders/{id}">conductor.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/purchase_order_delete_response.py">PurchaseOrderDeleteResponse</a></code>

## ReceivePayments

Types:

```python
from conductor.types.qbd import ReceivePayment, ReceivePaymentDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/receive-payments">conductor.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">create</a>(\*\*<a href="src/conductor/types/qbd/receive_payment_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/receive_payment.py">ReceivePayment</a></code>
- <code title="get /quickbooks-desktop/receive-payments/{id}">conductor.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/receive_payment.py">ReceivePayment</a></code>
- <code title="post /quickbooks-desktop/receive-payments/{id}">conductor.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/receive_payment_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/receive_payment.py">ReceivePayment</a></code>
- <code title="get /quickbooks-desktop/receive-payments">conductor.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">list</a>(\*\*<a href="src/conductor/types/qbd/receive_payment_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/receive_payment.py">SyncCursorPage[ReceivePayment]</a></code>
- <code title="delete /quickbooks-desktop/receive-payments/{id}">conductor.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/receive_payment_delete_response.py">ReceivePaymentDeleteResponse</a></code>

## SalesOrders

Types:

```python
from conductor.types.qbd import SalesOrder, SalesOrderDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/sales-orders">conductor.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_order_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_order.py">SalesOrder</a></code>
- <code title="get /quickbooks-desktop/sales-orders/{id}">conductor.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_order.py">SalesOrder</a></code>
- <code title="post /quickbooks-desktop/sales-orders/{id}">conductor.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_order_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_order.py">SalesOrder</a></code>
- <code title="get /quickbooks-desktop/sales-orders">conductor.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_order_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_order.py">SyncCursorPage[SalesOrder]</a></code>
- <code title="delete /quickbooks-desktop/sales-orders/{id}">conductor.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/sales_order_delete_response.py">SalesOrderDeleteResponse</a></code>

## SalesReceipts

Types:

```python
from conductor.types.qbd import SalesReceipt, SalesReceiptDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/sales-receipts">conductor.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_receipt_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_receipt.py">SalesReceipt</a></code>
- <code title="get /quickbooks-desktop/sales-receipts/{id}">conductor.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_receipt.py">SalesReceipt</a></code>
- <code title="post /quickbooks-desktop/sales-receipts/{id}">conductor.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_receipt_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_receipt.py">SalesReceipt</a></code>
- <code title="get /quickbooks-desktop/sales-receipts">conductor.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_receipt_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_receipt.py">SyncCursorPage[SalesReceipt]</a></code>
- <code title="delete /quickbooks-desktop/sales-receipts/{id}">conductor.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/sales_receipt_delete_response.py">SalesReceiptDeleteResponse</a></code>

## SalesRepresentatives

Types:

```python
from conductor.types.qbd import SalesRepresentative, SalesRepresentativeListResponse
```

Methods:

- <code title="post /quickbooks-desktop/sales-representatives">conductor.qbd.sales_representatives.<a href="./src/conductor/resources/qbd/sales_representatives.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_representative_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_representative.py">SalesRepresentative</a></code>
- <code title="get /quickbooks-desktop/sales-representatives/{id}">conductor.qbd.sales_representatives.<a href="./src/conductor/resources/qbd/sales_representatives.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_representative.py">SalesRepresentative</a></code>
- <code title="post /quickbooks-desktop/sales-representatives/{id}">conductor.qbd.sales_representatives.<a href="./src/conductor/resources/qbd/sales_representatives.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_representative_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_representative.py">SalesRepresentative</a></code>
- <code title="get /quickbooks-desktop/sales-representatives">conductor.qbd.sales_representatives.<a href="./src/conductor/resources/qbd/sales_representatives.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_representative_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_representative_list_response.py">SalesRepresentativeListResponse</a></code>

## SalesTaxCodes

Types:

```python
from conductor.types.qbd import SalesTaxCode, SalesTaxCodeListResponse
```

Methods:

- <code title="post /quickbooks-desktop/sales-tax-codes">conductor.qbd.sales_tax_codes.<a href="./src/conductor/resources/qbd/sales_tax_codes.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_tax_code_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_code.py">SalesTaxCode</a></code>
- <code title="get /quickbooks-desktop/sales-tax-codes/{id}">conductor.qbd.sales_tax_codes.<a href="./src/conductor/resources/qbd/sales_tax_codes.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_tax_code.py">SalesTaxCode</a></code>
- <code title="post /quickbooks-desktop/sales-tax-codes/{id}">conductor.qbd.sales_tax_codes.<a href="./src/conductor/resources/qbd/sales_tax_codes.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_tax_code_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_code.py">SalesTaxCode</a></code>
- <code title="get /quickbooks-desktop/sales-tax-codes">conductor.qbd.sales_tax_codes.<a href="./src/conductor/resources/qbd/sales_tax_codes.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_tax_code_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_code_list_response.py">SalesTaxCodeListResponse</a></code>

## SalesTaxItems

Types:

```python
from conductor.types.qbd import SalesTaxItem
```

Methods:

- <code title="post /quickbooks-desktop/sales-tax-items">conductor.qbd.sales_tax_items.<a href="./src/conductor/resources/qbd/sales_tax_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_tax_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_item.py">SalesTaxItem</a></code>
- <code title="get /quickbooks-desktop/sales-tax-items/{id}">conductor.qbd.sales_tax_items.<a href="./src/conductor/resources/qbd/sales_tax_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_tax_item.py">SalesTaxItem</a></code>
- <code title="post /quickbooks-desktop/sales-tax-items/{id}">conductor.qbd.sales_tax_items.<a href="./src/conductor/resources/qbd/sales_tax_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_tax_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_item.py">SalesTaxItem</a></code>
- <code title="get /quickbooks-desktop/sales-tax-items">conductor.qbd.sales_tax_items.<a href="./src/conductor/resources/qbd/sales_tax_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_tax_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_item.py">SyncCursorPage[SalesTaxItem]</a></code>

## ServiceItems

Types:

```python
from conductor.types.qbd import ServiceItem
```

Methods:

- <code title="post /quickbooks-desktop/service-items">conductor.qbd.service_items.<a href="./src/conductor/resources/qbd/service_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/service_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/service_item.py">ServiceItem</a></code>
- <code title="get /quickbooks-desktop/service-items/{id}">conductor.qbd.service_items.<a href="./src/conductor/resources/qbd/service_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/service_item.py">ServiceItem</a></code>
- <code title="post /quickbooks-desktop/service-items/{id}">conductor.qbd.service_items.<a href="./src/conductor/resources/qbd/service_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/service_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/service_item.py">ServiceItem</a></code>
- <code title="get /quickbooks-desktop/service-items">conductor.qbd.service_items.<a href="./src/conductor/resources/qbd/service_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/service_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/service_item.py">SyncCursorPage[ServiceItem]</a></code>

## StandardTerms

Types:

```python
from conductor.types.qbd import StandardTerm, StandardTermListResponse
```

Methods:

- <code title="post /quickbooks-desktop/standard-terms">conductor.qbd.standard_terms.<a href="./src/conductor/resources/qbd/standard_terms.py">create</a>(\*\*<a href="src/conductor/types/qbd/standard_term_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/standard_term.py">StandardTerm</a></code>
- <code title="get /quickbooks-desktop/standard-terms/{id}">conductor.qbd.standard_terms.<a href="./src/conductor/resources/qbd/standard_terms.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/standard_term.py">StandardTerm</a></code>
- <code title="get /quickbooks-desktop/standard-terms">conductor.qbd.standard_terms.<a href="./src/conductor/resources/qbd/standard_terms.py">list</a>(\*\*<a href="src/conductor/types/qbd/standard_term_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/standard_term_list_response.py">StandardTermListResponse</a></code>

## SubtotalItems

Types:

```python
from conductor.types.qbd import SubtotalItem
```

Methods:

- <code title="post /quickbooks-desktop/subtotal-items">conductor.qbd.subtotal_items.<a href="./src/conductor/resources/qbd/subtotal_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/subtotal_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/subtotal_item.py">SubtotalItem</a></code>
- <code title="get /quickbooks-desktop/subtotal-items/{id}">conductor.qbd.subtotal_items.<a href="./src/conductor/resources/qbd/subtotal_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/subtotal_item.py">SubtotalItem</a></code>
- <code title="post /quickbooks-desktop/subtotal-items/{id}">conductor.qbd.subtotal_items.<a href="./src/conductor/resources/qbd/subtotal_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/subtotal_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/subtotal_item.py">SubtotalItem</a></code>
- <code title="get /quickbooks-desktop/subtotal-items">conductor.qbd.subtotal_items.<a href="./src/conductor/resources/qbd/subtotal_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/subtotal_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/subtotal_item.py">SyncCursorPage[SubtotalItem]</a></code>

## Templates

Types:

```python
from conductor.types.qbd import Template, TemplateListResponse
```

Methods:

- <code title="get /quickbooks-desktop/templates">conductor.qbd.templates.<a href="./src/conductor/resources/qbd/templates.py">list</a>() -> <a href="./src/conductor/types/qbd/template_list_response.py">TemplateListResponse</a></code>

## TimeTrackingActivities

Types:

```python
from conductor.types.qbd import TimeTrackingActivity, TimeTrackingActivityDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/time-tracking-activities">conductor.qbd.time_tracking_activities.<a href="./src/conductor/resources/qbd/time_tracking_activities.py">create</a>(\*\*<a href="src/conductor/types/qbd/time_tracking_activity_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/time_tracking_activity.py">TimeTrackingActivity</a></code>
- <code title="get /quickbooks-desktop/time-tracking-activities/{id}">conductor.qbd.time_tracking_activities.<a href="./src/conductor/resources/qbd/time_tracking_activities.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/time_tracking_activity.py">TimeTrackingActivity</a></code>
- <code title="post /quickbooks-desktop/time-tracking-activities/{id}">conductor.qbd.time_tracking_activities.<a href="./src/conductor/resources/qbd/time_tracking_activities.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/time_tracking_activity_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/time_tracking_activity.py">TimeTrackingActivity</a></code>
- <code title="get /quickbooks-desktop/time-tracking-activities">conductor.qbd.time_tracking_activities.<a href="./src/conductor/resources/qbd/time_tracking_activities.py">list</a>(\*\*<a href="src/conductor/types/qbd/time_tracking_activity_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/time_tracking_activity.py">SyncCursorPage[TimeTrackingActivity]</a></code>
- <code title="delete /quickbooks-desktop/time-tracking-activities/{id}">conductor.qbd.time_tracking_activities.<a href="./src/conductor/resources/qbd/time_tracking_activities.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/time_tracking_activity_delete_response.py">TimeTrackingActivityDeleteResponse</a></code>

## Transactions

Types:

```python
from conductor.types.qbd import Transaction
```

Methods:

- <code title="get /quickbooks-desktop/transactions/{id}">conductor.qbd.transactions.<a href="./src/conductor/resources/qbd/transactions.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/transaction.py">Transaction</a></code>
- <code title="get /quickbooks-desktop/transactions">conductor.qbd.transactions.<a href="./src/conductor/resources/qbd/transactions.py">list</a>(\*\*<a href="src/conductor/types/qbd/transaction_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/transaction.py">SyncCursorPage[Transaction]</a></code>

## Transfers

Types:

```python
from conductor.types.qbd import Transfer
```

Methods:

- <code title="post /quickbooks-desktop/transfers">conductor.qbd.transfers.<a href="./src/conductor/resources/qbd/transfers.py">create</a>(\*\*<a href="src/conductor/types/qbd/transfer_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/transfer.py">Transfer</a></code>
- <code title="get /quickbooks-desktop/transfers/{id}">conductor.qbd.transfers.<a href="./src/conductor/resources/qbd/transfers.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/transfer.py">Transfer</a></code>
- <code title="post /quickbooks-desktop/transfers/{id}">conductor.qbd.transfers.<a href="./src/conductor/resources/qbd/transfers.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/transfer_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/transfer.py">Transfer</a></code>
- <code title="get /quickbooks-desktop/transfers">conductor.qbd.transfers.<a href="./src/conductor/resources/qbd/transfers.py">list</a>(\*\*<a href="src/conductor/types/qbd/transfer_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/transfer.py">SyncCursorPage[Transfer]</a></code>

## UnitOfMeasureSets

Types:

```python
from conductor.types.qbd import UnitOfMeasureSet, UnitOfMeasureSetListResponse
```

Methods:

- <code title="post /quickbooks-desktop/unit-of-measure-sets">conductor.qbd.unit_of_measure_sets.<a href="./src/conductor/resources/qbd/unit_of_measure_sets.py">create</a>(\*\*<a href="src/conductor/types/qbd/unit_of_measure_set_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/unit_of_measure_set.py">UnitOfMeasureSet</a></code>
- <code title="get /quickbooks-desktop/unit-of-measure-sets/{id}">conductor.qbd.unit_of_measure_sets.<a href="./src/conductor/resources/qbd/unit_of_measure_sets.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/unit_of_measure_set.py">UnitOfMeasureSet</a></code>
- <code title="get /quickbooks-desktop/unit-of-measure-sets">conductor.qbd.unit_of_measure_sets.<a href="./src/conductor/resources/qbd/unit_of_measure_sets.py">list</a>(\*\*<a href="src/conductor/types/qbd/unit_of_measure_set_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/unit_of_measure_set_list_response.py">UnitOfMeasureSetListResponse</a></code>

## VendorCredits

Types:

```python
from conductor.types.qbd import VendorCredit, VendorCreditDeleteResponse
```

Methods:

- <code title="post /quickbooks-desktop/vendor-credits">conductor.qbd.vendor_credits.<a href="./src/conductor/resources/qbd/vendor_credits.py">create</a>(\*\*<a href="src/conductor/types/qbd/vendor_credit_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor_credit.py">VendorCredit</a></code>
- <code title="get /quickbooks-desktop/vendor-credits/{id}">conductor.qbd.vendor_credits.<a href="./src/conductor/resources/qbd/vendor_credits.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/vendor_credit.py">VendorCredit</a></code>
- <code title="post /quickbooks-desktop/vendor-credits/{id}">conductor.qbd.vendor_credits.<a href="./src/conductor/resources/qbd/vendor_credits.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/vendor_credit_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor_credit.py">VendorCredit</a></code>
- <code title="get /quickbooks-desktop/vendor-credits">conductor.qbd.vendor_credits.<a href="./src/conductor/resources/qbd/vendor_credits.py">list</a>(\*\*<a href="src/conductor/types/qbd/vendor_credit_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor_credit.py">SyncCursorPage[VendorCredit]</a></code>
- <code title="delete /quickbooks-desktop/vendor-credits/{id}">conductor.qbd.vendor_credits.<a href="./src/conductor/resources/qbd/vendor_credits.py">delete</a>(id) -> <a href="./src/conductor/types/qbd/vendor_credit_delete_response.py">VendorCreditDeleteResponse</a></code>

## Vendors

Types:

```python
from conductor.types.qbd import Vendor
```

Methods:

- <code title="post /quickbooks-desktop/vendors">conductor.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">create</a>(\*\*<a href="src/conductor/types/qbd/vendor_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor.py">Vendor</a></code>
- <code title="get /quickbooks-desktop/vendors/{id}">conductor.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/vendor.py">Vendor</a></code>
- <code title="post /quickbooks-desktop/vendors/{id}">conductor.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/vendor_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor.py">Vendor</a></code>
- <code title="get /quickbooks-desktop/vendors">conductor.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">list</a>(\*\*<a href="src/conductor/types/qbd/vendor_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor.py">SyncCursorPage[Vendor]</a></code>
