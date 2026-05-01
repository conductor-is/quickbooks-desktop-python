# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    Deposit,
    DepositVoidResponse,
    DepositDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeposits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.create(
            deposit_to_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.create(
            deposit_to_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            cash_back={
                "account_id": "80000001-1234567890",
                "amount": "1000.00",
                "memo": "Cash back from deposit",
            },
            currency_id="80000001-1234567890",
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            lines=[
                {
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "check_number": "1234567890",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "memo": "Payment batched into settlement deposit",
                    "override_check_number": "1234567890",
                    "override_class_id": "80000001-1234567890",
                    "override_memo": "Batch settlement deposit",
                    "payment_method_id": "80000001-1234567890",
                    "payment_transaction_id": "123ABC-1234567890",
                    "payment_transaction_line_id": "456DEF-1234567890",
                }
            ],
            memo="Batch settlement deposit",
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.deposits.with_raw_response.create(
            deposit_to_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = response.parse()
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.deposits.with_streaming_response.create(
            deposit_to_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = response.parse()
            assert_matches_type(Deposit, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.deposits.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = response.parse()
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.deposits.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = response.parse()
            assert_matches_type(Deposit, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.deposits.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            cash_back={
                "account_id": "80000001-1234567890",
                "amount": "1000.00",
                "memo": "Cash back from deposit",
            },
            currency_id="80000001-1234567890",
            deposit_to_account_id="80000001-1234567890",
            exchange_rate=1.2345,
            lines=[
                {
                    "id": "456DEF-1234567890",
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "check_number": "1234567890",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "memo": "Payment batched into settlement deposit",
                    "override_check_number": "1234567890",
                    "override_class_id": "80000001-1234567890",
                    "override_memo": "Batch settlement deposit",
                    "payment_method_id": "80000001-1234567890",
                    "payment_transaction_id": "123ABC-1234567890",
                    "payment_transaction_line_id": "456DEF-1234567890",
                }
            ],
            memo="Batch settlement deposit",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.deposits.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = response.parse()
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.deposits.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = response.parse()
            assert_matches_type(Deposit, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.deposits.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[Deposit], deposit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            entity_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[Deposit], deposit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.deposits.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = response.parse()
        assert_matches_type(SyncCursorPage[Deposit], deposit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.deposits.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = response.parse()
            assert_matches_type(SyncCursorPage[Deposit], deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(DepositDeleteResponse, deposit, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.deposits.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = response.parse()
        assert_matches_type(DepositDeleteResponse, deposit, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.deposits.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = response.parse()
            assert_matches_type(DepositDeleteResponse, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.deposits.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_void(self, client: Conductor) -> None:
        deposit = client.qbd.deposits.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(DepositVoidResponse, deposit, path=["response"])

    @parametrize
    def test_raw_response_void(self, client: Conductor) -> None:
        response = client.qbd.deposits.with_raw_response.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = response.parse()
        assert_matches_type(DepositVoidResponse, deposit, path=["response"])

    @parametrize
    def test_streaming_response_void(self, client: Conductor) -> None:
        with client.qbd.deposits.with_streaming_response.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = response.parse()
            assert_matches_type(DepositVoidResponse, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_void(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.deposits.with_raw_response.void(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncDeposits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.create(
            deposit_to_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.create(
            deposit_to_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            cash_back={
                "account_id": "80000001-1234567890",
                "amount": "1000.00",
                "memo": "Cash back from deposit",
            },
            currency_id="80000001-1234567890",
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            lines=[
                {
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "check_number": "1234567890",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "memo": "Payment batched into settlement deposit",
                    "override_check_number": "1234567890",
                    "override_class_id": "80000001-1234567890",
                    "override_memo": "Batch settlement deposit",
                    "payment_method_id": "80000001-1234567890",
                    "payment_transaction_id": "123ABC-1234567890",
                    "payment_transaction_line_id": "456DEF-1234567890",
                }
            ],
            memo="Batch settlement deposit",
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.deposits.with_raw_response.create(
            deposit_to_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = await response.parse()
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.deposits.with_streaming_response.create(
            deposit_to_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = await response.parse()
            assert_matches_type(Deposit, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.deposits.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = await response.parse()
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.deposits.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = await response.parse()
            assert_matches_type(Deposit, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.deposits.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            cash_back={
                "account_id": "80000001-1234567890",
                "amount": "1000.00",
                "memo": "Cash back from deposit",
            },
            currency_id="80000001-1234567890",
            deposit_to_account_id="80000001-1234567890",
            exchange_rate=1.2345,
            lines=[
                {
                    "id": "456DEF-1234567890",
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "check_number": "1234567890",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "memo": "Payment batched into settlement deposit",
                    "override_check_number": "1234567890",
                    "override_class_id": "80000001-1234567890",
                    "override_memo": "Batch settlement deposit",
                    "payment_method_id": "80000001-1234567890",
                    "payment_transaction_id": "123ABC-1234567890",
                    "payment_transaction_line_id": "456DEF-1234567890",
                }
            ],
            memo="Batch settlement deposit",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.deposits.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = await response.parse()
        assert_matches_type(Deposit, deposit, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.deposits.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = await response.parse()
            assert_matches_type(Deposit, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.deposits.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[Deposit], deposit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            entity_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[Deposit], deposit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.deposits.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = await response.parse()
        assert_matches_type(AsyncCursorPage[Deposit], deposit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.deposits.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = await response.parse()
            assert_matches_type(AsyncCursorPage[Deposit], deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(DepositDeleteResponse, deposit, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.deposits.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = await response.parse()
        assert_matches_type(DepositDeleteResponse, deposit, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.deposits.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = await response.parse()
            assert_matches_type(DepositDeleteResponse, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.deposits.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_void(self, async_client: AsyncConductor) -> None:
        deposit = await async_client.qbd.deposits.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(DepositVoidResponse, deposit, path=["response"])

    @parametrize
    async def test_raw_response_void(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.deposits.with_raw_response.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deposit = await response.parse()
        assert_matches_type(DepositVoidResponse, deposit, path=["response"])

    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.deposits.with_streaming_response.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deposit = await response.parse()
            assert_matches_type(DepositVoidResponse, deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_void(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.deposits.with_raw_response.void(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
