# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import Transaction
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        transaction = client.qbd.transactions.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.transactions.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.transactions.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.transactions.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        transaction = client.qbd.transactions.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        transaction = client.qbd.transactions.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            class_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            detail_level="transactions_without_lines",
            entity_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            item_ids=["80000001-1234567890"],
            limit=150,
            payment_status="open",
            posting_status="posting",
            ref_number_contains="INV-1234",
            ref_number_ends_with="1234",
            ref_number_from="INV-0001",
            ref_numbers=["TRANSACTION-1234"],
            ref_number_starts_with="INV",
            ref_number_to="INV-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            transaction_types=["invoice"],
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.transactions.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(SyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.transactions.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(SyncCursorPage[Transaction], transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        transaction = await async_client.qbd.transactions.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.transactions.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.transactions.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.transactions.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        transaction = await async_client.qbd.transactions.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        transaction = await async_client.qbd.transactions.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            class_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            detail_level="transactions_without_lines",
            entity_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            item_ids=["80000001-1234567890"],
            limit=150,
            payment_status="open",
            posting_status="posting",
            ref_number_contains="INV-1234",
            ref_number_ends_with="1234",
            ref_number_from="INV-0001",
            ref_numbers=["TRANSACTION-1234"],
            ref_number_starts_with="INV",
            ref_number_to="INV-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            transaction_types=["invoice"],
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.transactions.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(AsyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.transactions.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(AsyncCursorPage[Transaction], transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
