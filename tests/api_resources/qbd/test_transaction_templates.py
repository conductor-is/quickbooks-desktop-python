# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import TransactionTemplateListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactionTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        transaction_template = client.qbd.transaction_templates.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TransactionTemplateListResponse, transaction_template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.transaction_templates.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction_template = response.parse()
        assert_matches_type(TransactionTemplateListResponse, transaction_template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.transaction_templates.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction_template = response.parse()
            assert_matches_type(TransactionTemplateListResponse, transaction_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactionTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        transaction_template = await async_client.qbd.transaction_templates.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(TransactionTemplateListResponse, transaction_template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.transaction_templates.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction_template = await response.parse()
        assert_matches_type(TransactionTemplateListResponse, transaction_template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.transaction_templates.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction_template = await response.parse()
            assert_matches_type(TransactionTemplateListResponse, transaction_template, path=["response"])

        assert cast(Any, response.is_closed) is True
