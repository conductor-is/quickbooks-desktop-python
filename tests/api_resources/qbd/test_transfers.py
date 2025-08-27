# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import Transfer
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        transfer = client.qbd.transfers.create(
            amount="1000.00",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        transfer = client.qbd.transfers.create(
            amount="1000.00",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_id="80000001-1234567890",
            memo="Monthly transfer to savings",
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.transfers.with_raw_response.create(
            amount="1000.00",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.transfers.with_streaming_response.create(
            amount="1000.00",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(Transfer, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        transfer = client.qbd.transfers.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.transfers.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.transfers.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(Transfer, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.transfers.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        transfer = client.qbd.transfers.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        transfer = client.qbd.transfers.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            amount="1000.00",
            class_id="80000001-1234567890",
            memo="Monthly transfer to savings",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.transfers.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.transfers.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(Transfer, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.transfers.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        transfer = client.qbd.transfers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[Transfer], transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        transfer = client.qbd.transfers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            limit=150,
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[Transfer], transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.transfers.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(SyncCursorPage[Transfer], transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.transfers.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(SyncCursorPage[Transfer], transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        transfer = await async_client.qbd.transfers.create(
            amount="1000.00",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        transfer = await async_client.qbd.transfers.create(
            amount="1000.00",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_id="80000001-1234567890",
            memo="Monthly transfer to savings",
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.transfers.with_raw_response.create(
            amount="1000.00",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.transfers.with_streaming_response.create(
            amount="1000.00",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(Transfer, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        transfer = await async_client.qbd.transfers.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.transfers.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.transfers.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(Transfer, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.transfers.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        transfer = await async_client.qbd.transfers.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        transfer = await async_client.qbd.transfers.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            amount="1000.00",
            class_id="80000001-1234567890",
            memo="Monthly transfer to savings",
            source_account_id="80000001-1234567890",
            target_account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.transfers.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(Transfer, transfer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.transfers.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(Transfer, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.transfers.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        transfer = await async_client.qbd.transfers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[Transfer], transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        transfer = await async_client.qbd.transfers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            limit=150,
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[Transfer], transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.transfers.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(AsyncCursorPage[Transfer], transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.transfers.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(AsyncCursorPage[Transfer], transfer, path=["response"])

        assert cast(Any, response.is_closed) is True
