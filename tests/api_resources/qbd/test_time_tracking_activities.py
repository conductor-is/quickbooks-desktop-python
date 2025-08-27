# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    TimeTrackingActivity,
    TimeTrackingActivityDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeTrackingActivities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        time_tracking_activity = client.qbd.time_tracking_activities.create(
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        time_tracking_activity = client.qbd.time_tracking_activities.create(
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            billing_status="billable",
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            note="Project planning meeting with client.",
            payroll_wage_item_id="80000001-1234567890",
            service_item_id="80000001-1234567890",
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.time_tracking_activities.with_raw_response.create(
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = response.parse()
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.time_tracking_activities.with_streaming_response.create(
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = response.parse()
            assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        time_tracking_activity = client.qbd.time_tracking_activities.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.time_tracking_activities.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = response.parse()
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.time_tracking_activities.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = response.parse()
            assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.time_tracking_activities.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        time_tracking_activity = client.qbd.time_tracking_activities.update(
            id="123ABC-1234567890",
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        time_tracking_activity = client.qbd.time_tracking_activities.update(
            id="123ABC-1234567890",
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            billing_status="billable",
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            note="Project planning meeting with client.",
            payroll_wage_item_id="80000001-1234567890",
            service_item_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.time_tracking_activities.with_raw_response.update(
            id="123ABC-1234567890",
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = response.parse()
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.time_tracking_activities.with_streaming_response.update(
            id="123ABC-1234567890",
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = response.parse()
            assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.time_tracking_activities.with_raw_response.update(
                id="",
                duration="PT1H30M",
                entity_id="80000001-1234567890",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        time_tracking_activity = client.qbd.time_tracking_activities.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[TimeTrackingActivity], time_tracking_activity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        time_tracking_activity = client.qbd.time_tracking_activities.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            entity_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            limit=150,
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[TimeTrackingActivity], time_tracking_activity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.time_tracking_activities.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = response.parse()
        assert_matches_type(SyncCursorPage[TimeTrackingActivity], time_tracking_activity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.time_tracking_activities.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = response.parse()
            assert_matches_type(SyncCursorPage[TimeTrackingActivity], time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        time_tracking_activity = client.qbd.time_tracking_activities.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TimeTrackingActivityDeleteResponse, time_tracking_activity, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.time_tracking_activities.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = response.parse()
        assert_matches_type(TimeTrackingActivityDeleteResponse, time_tracking_activity, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.time_tracking_activities.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = response.parse()
            assert_matches_type(TimeTrackingActivityDeleteResponse, time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.time_tracking_activities.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncTimeTrackingActivities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        time_tracking_activity = await async_client.qbd.time_tracking_activities.create(
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        time_tracking_activity = await async_client.qbd.time_tracking_activities.create(
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            billing_status="billable",
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            note="Project planning meeting with client.",
            payroll_wage_item_id="80000001-1234567890",
            service_item_id="80000001-1234567890",
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.time_tracking_activities.with_raw_response.create(
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = await response.parse()
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.time_tracking_activities.with_streaming_response.create(
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = await response.parse()
            assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        time_tracking_activity = await async_client.qbd.time_tracking_activities.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.time_tracking_activities.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = await response.parse()
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.time_tracking_activities.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = await response.parse()
            assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.time_tracking_activities.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        time_tracking_activity = await async_client.qbd.time_tracking_activities.update(
            id="123ABC-1234567890",
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        time_tracking_activity = await async_client.qbd.time_tracking_activities.update(
            id="123ABC-1234567890",
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            billing_status="billable",
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            note="Project planning meeting with client.",
            payroll_wage_item_id="80000001-1234567890",
            service_item_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.time_tracking_activities.with_raw_response.update(
            id="123ABC-1234567890",
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = await response.parse()
        assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.time_tracking_activities.with_streaming_response.update(
            id="123ABC-1234567890",
            duration="PT1H30M",
            entity_id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = await response.parse()
            assert_matches_type(TimeTrackingActivity, time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.time_tracking_activities.with_raw_response.update(
                id="",
                duration="PT1H30M",
                entity_id="80000001-1234567890",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        time_tracking_activity = await async_client.qbd.time_tracking_activities.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[TimeTrackingActivity], time_tracking_activity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        time_tracking_activity = await async_client.qbd.time_tracking_activities.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            entity_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            limit=150,
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[TimeTrackingActivity], time_tracking_activity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.time_tracking_activities.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = await response.parse()
        assert_matches_type(AsyncCursorPage[TimeTrackingActivity], time_tracking_activity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.time_tracking_activities.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = await response.parse()
            assert_matches_type(AsyncCursorPage[TimeTrackingActivity], time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        time_tracking_activity = await async_client.qbd.time_tracking_activities.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TimeTrackingActivityDeleteResponse, time_tracking_activity, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.time_tracking_activities.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_tracking_activity = await response.parse()
        assert_matches_type(TimeTrackingActivityDeleteResponse, time_tracking_activity, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.time_tracking_activities.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_tracking_activity = await response.parse()
            assert_matches_type(TimeTrackingActivityDeleteResponse, time_tracking_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.time_tracking_activities.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
