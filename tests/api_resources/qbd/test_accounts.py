# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    Account,
    AccountListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        account = client.qbd.accounts.create(
            account_type="bank",
            name="Accounts-Payable",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        account = client.qbd.accounts.create(
            account_type="bank",
            name="Accounts-Payable",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            bank_account_number="123456789",
            currency_id="80000001-1234567890",
            description="Accounts-payable are the amounts owed to suppliers for goods and services purchased on credit.",
            is_active=True,
            opening_balance="1000.00",
            opening_balance_date=parse_date("2023-01-01"),
            parent_id="80000001-1234567890",
            sales_tax_code_id="80000001-1234567890",
            tax_line_id=123,
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.accounts.with_raw_response.create(
            account_type="bank",
            name="Accounts-Payable",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.accounts.with_streaming_response.create(
            account_type="bank",
            name="Accounts-Payable",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        account = client.qbd.accounts.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.accounts.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.accounts.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.accounts.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        account = client.qbd.accounts.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        account = client.qbd.accounts.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            account_type="bank",
            bank_account_number="123456789",
            currency_id="80000001-1234567890",
            description="Accounts-payable are the amounts owed to suppliers for goods and services purchased on credit.",
            is_active=True,
            name="Accounts-Payable",
            opening_balance="1000.00",
            opening_balance_date=parse_date("2023-01-01"),
            parent_id="80000001-1234567890",
            sales_tax_code_id="80000001-1234567890",
            tax_line_id=123,
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.accounts.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.accounts.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.accounts.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        account = client.qbd.accounts.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        account = client.qbd.accounts.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_type="income",
            currency_ids=["80000001-1234567890"],
            full_names=["Corporate:Accounts-Payable"],
            ids=["80000001-1234567890"],
            limit=10,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.accounts.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.accounts.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        account = await async_client.qbd.accounts.create(
            account_type="bank",
            name="Accounts-Payable",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        account = await async_client.qbd.accounts.create(
            account_type="bank",
            name="Accounts-Payable",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            bank_account_number="123456789",
            currency_id="80000001-1234567890",
            description="Accounts-payable are the amounts owed to suppliers for goods and services purchased on credit.",
            is_active=True,
            opening_balance="1000.00",
            opening_balance_date=parse_date("2023-01-01"),
            parent_id="80000001-1234567890",
            sales_tax_code_id="80000001-1234567890",
            tax_line_id=123,
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.accounts.with_raw_response.create(
            account_type="bank",
            name="Accounts-Payable",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.accounts.with_streaming_response.create(
            account_type="bank",
            name="Accounts-Payable",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        account = await async_client.qbd.accounts.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.accounts.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.accounts.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.accounts.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        account = await async_client.qbd.accounts.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        account = await async_client.qbd.accounts.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            account_type="bank",
            bank_account_number="123456789",
            currency_id="80000001-1234567890",
            description="Accounts-payable are the amounts owed to suppliers for goods and services purchased on credit.",
            is_active=True,
            name="Accounts-Payable",
            opening_balance="1000.00",
            opening_balance_date=parse_date("2023-01-01"),
            parent_id="80000001-1234567890",
            sales_tax_code_id="80000001-1234567890",
            tax_line_id=123,
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.accounts.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.accounts.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.accounts.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        account = await async_client.qbd.accounts.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        account = await async_client.qbd.accounts.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_type="income",
            currency_ids=["80000001-1234567890"],
            full_names=["Corporate:Accounts-Payable"],
            ids=["80000001-1234567890"],
            limit=10,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.accounts.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.accounts.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
