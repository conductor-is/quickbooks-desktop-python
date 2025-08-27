# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    JournalEntry,
    JournalEntryDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJournalEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        journal_entry = client.qbd.journal_entries.create(
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        journal_entry = client.qbd.journal_entries.create(
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            are_amounts_entered_in_home_currency=False,
            credit_lines=[
                {
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "memo": "Allocated funds for office lease payment",
                    "sales_tax_item_id": "80000001-1234567890",
                }
            ],
            currency_id="80000001-1234567890",
            debit_lines=[
                {
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "memo": "Monthly utility bill settlement",
                    "sales_tax_item_id": "80000001-1234567890",
                }
            ],
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_adjustment=False,
            is_home_currency_adjustment=False,
            ref_number="JE-1234",
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.journal_entries.with_raw_response.create(
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = response.parse()
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.journal_entries.with_streaming_response.create(
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = response.parse()
            assert_matches_type(JournalEntry, journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        journal_entry = client.qbd.journal_entries.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.journal_entries.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = response.parse()
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.journal_entries.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = response.parse()
            assert_matches_type(JournalEntry, journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.journal_entries.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        journal_entry = client.qbd.journal_entries.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        journal_entry = client.qbd.journal_entries.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            are_amounts_entered_in_home_currency=False,
            currency_id="80000001-1234567890",
            exchange_rate=1.2345,
            is_adjustment=False,
            lines=[
                {
                    "id": "456DEF-1234567890",
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "journal_line_type": "debit",
                    "memo": "Allocated funds for office lease payment",
                    "sales_tax_item_id": "80000001-1234567890",
                }
            ],
            ref_number="JE-1234",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.journal_entries.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = response.parse()
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.journal_entries.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = response.parse()
            assert_matches_type(JournalEntry, journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.journal_entries.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        journal_entry = client.qbd.journal_entries.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[JournalEntry], journal_entry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        journal_entry = client.qbd.journal_entries.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            entity_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="JE-1234",
            ref_number_ends_with="1234",
            ref_number_from="JE-0001",
            ref_numbers=["JOURNAL ENTRY-1234"],
            ref_number_starts_with="JE",
            ref_number_to="JE-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[JournalEntry], journal_entry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.journal_entries.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = response.parse()
        assert_matches_type(SyncCursorPage[JournalEntry], journal_entry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.journal_entries.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = response.parse()
            assert_matches_type(SyncCursorPage[JournalEntry], journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        journal_entry = client.qbd.journal_entries.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(JournalEntryDeleteResponse, journal_entry, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.journal_entries.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = response.parse()
        assert_matches_type(JournalEntryDeleteResponse, journal_entry, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.journal_entries.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = response.parse()
            assert_matches_type(JournalEntryDeleteResponse, journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.journal_entries.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncJournalEntries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        journal_entry = await async_client.qbd.journal_entries.create(
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        journal_entry = await async_client.qbd.journal_entries.create(
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            are_amounts_entered_in_home_currency=False,
            credit_lines=[
                {
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "memo": "Allocated funds for office lease payment",
                    "sales_tax_item_id": "80000001-1234567890",
                }
            ],
            currency_id="80000001-1234567890",
            debit_lines=[
                {
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "memo": "Monthly utility bill settlement",
                    "sales_tax_item_id": "80000001-1234567890",
                }
            ],
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_adjustment=False,
            is_home_currency_adjustment=False,
            ref_number="JE-1234",
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.journal_entries.with_raw_response.create(
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = await response.parse()
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.journal_entries.with_streaming_response.create(
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = await response.parse()
            assert_matches_type(JournalEntry, journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        journal_entry = await async_client.qbd.journal_entries.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.journal_entries.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = await response.parse()
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.journal_entries.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = await response.parse()
            assert_matches_type(JournalEntry, journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.journal_entries.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        journal_entry = await async_client.qbd.journal_entries.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        journal_entry = await async_client.qbd.journal_entries.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            are_amounts_entered_in_home_currency=False,
            currency_id="80000001-1234567890",
            exchange_rate=1.2345,
            is_adjustment=False,
            lines=[
                {
                    "id": "456DEF-1234567890",
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "entity_id": "80000001-1234567890",
                    "journal_line_type": "debit",
                    "memo": "Allocated funds for office lease payment",
                    "sales_tax_item_id": "80000001-1234567890",
                }
            ],
            ref_number="JE-1234",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.journal_entries.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = await response.parse()
        assert_matches_type(JournalEntry, journal_entry, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.journal_entries.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = await response.parse()
            assert_matches_type(JournalEntry, journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.journal_entries.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        journal_entry = await async_client.qbd.journal_entries.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[JournalEntry], journal_entry, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        journal_entry = await async_client.qbd.journal_entries.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            entity_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="JE-1234",
            ref_number_ends_with="1234",
            ref_number_from="JE-0001",
            ref_numbers=["JOURNAL ENTRY-1234"],
            ref_number_starts_with="JE",
            ref_number_to="JE-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[JournalEntry], journal_entry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.journal_entries.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = await response.parse()
        assert_matches_type(AsyncCursorPage[JournalEntry], journal_entry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.journal_entries.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = await response.parse()
            assert_matches_type(AsyncCursorPage[JournalEntry], journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        journal_entry = await async_client.qbd.journal_entries.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(JournalEntryDeleteResponse, journal_entry, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.journal_entries.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal_entry = await response.parse()
        assert_matches_type(JournalEntryDeleteResponse, journal_entry, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.journal_entries.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal_entry = await response.parse()
            assert_matches_type(JournalEntryDeleteResponse, journal_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.journal_entries.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
