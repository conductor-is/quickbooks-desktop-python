# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    BuildAssembly,
    BuildAssemblyDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuildAssemblies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        build_assembly = client.qbd.build_assemblies.create(
            inventory_assembly_item_id="80000001-1234567890",
            quantity_to_build=7,
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        build_assembly = client.qbd.build_assemblies.create(
            inventory_assembly_item_id="80000001-1234567890",
            quantity_to_build=7,
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            expiration_date=parse_date("2025-12-31"),
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            inventory_site_id="80000001-1234567890",
            inventory_site_location_id="80000001-1234567890",
            lot_number="LOT2023-001",
            mark_pending_if_required=True,
            memo="Assembled 25 units of Model ABC-123 Office Chair",
            ref_number="BUILD-1234",
            serial_number="SN1234567890",
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.build_assemblies.with_raw_response.create(
            inventory_assembly_item_id="80000001-1234567890",
            quantity_to_build=7,
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = response.parse()
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.build_assemblies.with_streaming_response.create(
            inventory_assembly_item_id="80000001-1234567890",
            quantity_to_build=7,
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = response.parse()
            assert_matches_type(BuildAssembly, build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        build_assembly = client.qbd.build_assemblies.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.build_assemblies.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = response.parse()
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.build_assemblies.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = response.parse()
            assert_matches_type(BuildAssembly, build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.build_assemblies.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        build_assembly = client.qbd.build_assemblies.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        build_assembly = client.qbd.build_assemblies.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            expiration_date=parse_date("2025-12-31"),
            inventory_site_id="80000001-1234567890",
            inventory_site_location_id="80000001-1234567890",
            lot_number="LOT2023-001",
            mark_pending_if_required=True,
            memo="Assembled 25 units of Model ABC-123 Office Chair",
            quantity_to_build=7,
            ref_number="BUILD-1234",
            remove_pending=True,
            serial_number="SN1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.build_assemblies.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = response.parse()
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.build_assemblies.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = response.parse()
            assert_matches_type(BuildAssembly, build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.build_assemblies.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        build_assembly = client.qbd.build_assemblies.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[BuildAssembly], build_assembly, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        build_assembly = client.qbd.build_assemblies.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_component_line_items=True,
            item_ids=["80000001-1234567890"],
            limit=150,
            pending_status="pending",
            ref_number_contains="BUILD-1234",
            ref_number_ends_with="1234",
            ref_number_from="BUILD-0001",
            ref_numbers=["BUILD ASSEMBLY-1234"],
            ref_number_starts_with="BUILD",
            ref_number_to="BUILD-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[BuildAssembly], build_assembly, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.build_assemblies.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = response.parse()
        assert_matches_type(SyncCursorPage[BuildAssembly], build_assembly, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.build_assemblies.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = response.parse()
            assert_matches_type(SyncCursorPage[BuildAssembly], build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        build_assembly = client.qbd.build_assemblies.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BuildAssemblyDeleteResponse, build_assembly, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.build_assemblies.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = response.parse()
        assert_matches_type(BuildAssemblyDeleteResponse, build_assembly, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.build_assemblies.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = response.parse()
            assert_matches_type(BuildAssemblyDeleteResponse, build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.build_assemblies.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncBuildAssemblies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        build_assembly = await async_client.qbd.build_assemblies.create(
            inventory_assembly_item_id="80000001-1234567890",
            quantity_to_build=7,
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        build_assembly = await async_client.qbd.build_assemblies.create(
            inventory_assembly_item_id="80000001-1234567890",
            quantity_to_build=7,
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            expiration_date=parse_date("2025-12-31"),
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            inventory_site_id="80000001-1234567890",
            inventory_site_location_id="80000001-1234567890",
            lot_number="LOT2023-001",
            mark_pending_if_required=True,
            memo="Assembled 25 units of Model ABC-123 Office Chair",
            ref_number="BUILD-1234",
            serial_number="SN1234567890",
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.build_assemblies.with_raw_response.create(
            inventory_assembly_item_id="80000001-1234567890",
            quantity_to_build=7,
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = await response.parse()
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.build_assemblies.with_streaming_response.create(
            inventory_assembly_item_id="80000001-1234567890",
            quantity_to_build=7,
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = await response.parse()
            assert_matches_type(BuildAssembly, build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        build_assembly = await async_client.qbd.build_assemblies.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.build_assemblies.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = await response.parse()
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.build_assemblies.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = await response.parse()
            assert_matches_type(BuildAssembly, build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.build_assemblies.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        build_assembly = await async_client.qbd.build_assemblies.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        build_assembly = await async_client.qbd.build_assemblies.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            expiration_date=parse_date("2025-12-31"),
            inventory_site_id="80000001-1234567890",
            inventory_site_location_id="80000001-1234567890",
            lot_number="LOT2023-001",
            mark_pending_if_required=True,
            memo="Assembled 25 units of Model ABC-123 Office Chair",
            quantity_to_build=7,
            ref_number="BUILD-1234",
            remove_pending=True,
            serial_number="SN1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.build_assemblies.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = await response.parse()
        assert_matches_type(BuildAssembly, build_assembly, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.build_assemblies.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = await response.parse()
            assert_matches_type(BuildAssembly, build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.build_assemblies.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        build_assembly = await async_client.qbd.build_assemblies.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[BuildAssembly], build_assembly, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        build_assembly = await async_client.qbd.build_assemblies.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_component_line_items=True,
            item_ids=["80000001-1234567890"],
            limit=150,
            pending_status="pending",
            ref_number_contains="BUILD-1234",
            ref_number_ends_with="1234",
            ref_number_from="BUILD-0001",
            ref_numbers=["BUILD ASSEMBLY-1234"],
            ref_number_starts_with="BUILD",
            ref_number_to="BUILD-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[BuildAssembly], build_assembly, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.build_assemblies.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = await response.parse()
        assert_matches_type(AsyncCursorPage[BuildAssembly], build_assembly, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.build_assemblies.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = await response.parse()
            assert_matches_type(AsyncCursorPage[BuildAssembly], build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        build_assembly = await async_client.qbd.build_assemblies.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BuildAssemblyDeleteResponse, build_assembly, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.build_assemblies.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_assembly = await response.parse()
        assert_matches_type(BuildAssemblyDeleteResponse, build_assembly, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.build_assemblies.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_assembly = await response.parse()
            assert_matches_type(BuildAssemblyDeleteResponse, build_assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.build_assemblies.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
