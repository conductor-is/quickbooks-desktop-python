# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import Customer
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        customer = client.qbd.customers.create(
            name="Website Redesign Project",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        customer = client.qbd.customers.create(
            name="Website Redesign Project",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_contacts=[
                {
                    "first_name": "John",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-123-4567",
                        }
                    ],
                    "job_title": "Purchasing Manager",
                    "last_name": "Doe",
                    "middle_name": "A.",
                    "salutation": "Dr.",
                }
            ],
            additional_notes=[{"note": "This is a fun note."}],
            alternate_contact="Bob Johnson",
            alternate_phone="+1-555-987-6543",
            alternate_shipping_addresses=[
                {
                    "name": "Alternate shipping address",
                    "city": "San Francisco",
                    "country": "United States",
                    "is_default_shipping_address": True,
                    "line1": "Conductor Labs Inc.",
                    "line2": "540 Market St.",
                    "line3": "Suite 100",
                    "line4": "",
                    "line5": "",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                }
            ],
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            cc_email="manager@example.com",
            class_id="80000001-1234567890",
            company_name="Acme Corporation",
            contact="Jane Smith",
            credit_card={
                "address": "1234 Main St, Anytown, USA, 12345",
                "expiration_month": 12,
                "expiration_year": 2024,
                "name": "John Doe",
                "number": "xxxxxxxxxxxx1234",
                "postal_code": "12345",
            },
            credit_limit="5000.00",
            currency_id="80000001-1234567890",
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                }
            ],
            customer_type_id="80000001-1234567890",
            email="customer@example.com",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            fax="+1-555-555-1212",
            first_name="John",
            is_active=True,
            job_description="Kitchen renovation project for residential client.",
            job_end_date=parse_date("2024-11-30"),
            job_projected_end_date=parse_date("2024-12-31"),
            job_start_date=parse_date("2024-01-15"),
            job_status="in_progress",
            job_title="Purchasing Manager",
            job_type_id="80000001-1234567890",
            last_name="Doe",
            middle_name="A.",
            note="Our favorite customer.",
            opening_balance="1000.00",
            opening_balance_date=parse_date("2023-01-01"),
            parent_id="80000001-1234567890",
            phone="+1-555-123-4567",
            preferred_delivery_method="email",
            preferred_payment_method_id="80000001-1234567890",
            price_level_id="80000001-1234567890",
            resale_number="123456789",
            sales_representative_id="80000001-1234567890",
            sales_tax_code_id="80000001-1234567890",
            sales_tax_country="us",
            sales_tax_item_id="80000001-1234567890",
            salutation="Dr.",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            tax_registration_number="GB123456789",
            terms_id="80000001-1234567890",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.customers.with_raw_response.create(
            name="Website Redesign Project",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.customers.with_streaming_response.create(
            name="Website Redesign Project",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        customer = client.qbd.customers.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.customers.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.customers.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.customers.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        customer = client.qbd.customers.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        customer = client.qbd.customers.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_contacts=[
                {
                    "id": "80000001-1234567890",
                    "revision_number": "1721172183",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-123-4567",
                        }
                    ],
                    "first_name": "John",
                    "job_title": "Purchasing Manager",
                    "last_name": "Doe",
                    "middle_name": "A.",
                    "salutation": "Dr.",
                }
            ],
            additional_notes=[
                {
                    "id": 1,
                    "note": "This is a fun note.",
                }
            ],
            alternate_contact="Bob Johnson",
            alternate_phone="+1-555-987-6543",
            alternate_shipping_addresses=[
                {
                    "name": "Alternate shipping address",
                    "city": "San Francisco",
                    "country": "United States",
                    "is_default_shipping_address": True,
                    "line1": "Conductor Labs Inc.",
                    "line2": "540 Market St.",
                    "line3": "Suite 100",
                    "line4": "",
                    "line5": "",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                }
            ],
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            cc_email="manager@example.com",
            class_id="80000001-1234567890",
            company_name="Acme Corporation",
            contact="Jane Smith",
            credit_card={
                "address": "1234 Main St, Anytown, USA, 12345",
                "expiration_month": 12,
                "expiration_year": 2024,
                "name": "John Doe",
                "number": "xxxxxxxxxxxx1234",
                "postal_code": "12345",
            },
            credit_limit="5000.00",
            currency_id="80000001-1234567890",
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                }
            ],
            customer_type_id="80000001-1234567890",
            email="customer@example.com",
            fax="+1-555-555-1212",
            first_name="John",
            is_active=True,
            job_description="Kitchen renovation project for residential client.",
            job_end_date=parse_date("2024-11-30"),
            job_projected_end_date=parse_date("2024-12-31"),
            job_start_date=parse_date("2024-01-15"),
            job_status="in_progress",
            job_title="Purchasing Manager",
            job_type_id="80000001-1234567890",
            last_name="Doe",
            middle_name="A.",
            name="Website Redesign Project",
            note="Our favorite customer.",
            parent_id="80000001-1234567890",
            phone="+1-555-123-4567",
            preferred_delivery_method="email",
            preferred_payment_method_id="80000001-1234567890",
            price_level_id="80000001-1234567890",
            resale_number="123456789",
            sales_representative_id="80000001-1234567890",
            sales_tax_code_id="80000001-1234567890",
            sales_tax_country="us",
            sales_tax_item_id="80000001-1234567890",
            salutation="Dr.",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            tax_registration_number="GB123456789",
            terms_id="80000001-1234567890",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.customers.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.customers.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.customers.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        customer = client.qbd.customers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[Customer], customer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        customer = client.qbd.customers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names=["ABC Corporation:Website Redesign Project"],
            ids=["80000001-1234567890"],
            limit=150,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            total_balance="123.45",
            total_balance_greater_than="123.45",
            total_balance_greater_than_or_equal_to="123.45",
            total_balance_less_than="123.45",
            total_balance_less_than_or_equal_to="123.45",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[Customer], customer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.customers.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncCursorPage[Customer], customer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.customers.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SyncCursorPage[Customer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.create(
            name="Website Redesign Project",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.create(
            name="Website Redesign Project",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_contacts=[
                {
                    "first_name": "John",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-123-4567",
                        }
                    ],
                    "job_title": "Purchasing Manager",
                    "last_name": "Doe",
                    "middle_name": "A.",
                    "salutation": "Dr.",
                }
            ],
            additional_notes=[{"note": "This is a fun note."}],
            alternate_contact="Bob Johnson",
            alternate_phone="+1-555-987-6543",
            alternate_shipping_addresses=[
                {
                    "name": "Alternate shipping address",
                    "city": "San Francisco",
                    "country": "United States",
                    "is_default_shipping_address": True,
                    "line1": "Conductor Labs Inc.",
                    "line2": "540 Market St.",
                    "line3": "Suite 100",
                    "line4": "",
                    "line5": "",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                }
            ],
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            cc_email="manager@example.com",
            class_id="80000001-1234567890",
            company_name="Acme Corporation",
            contact="Jane Smith",
            credit_card={
                "address": "1234 Main St, Anytown, USA, 12345",
                "expiration_month": 12,
                "expiration_year": 2024,
                "name": "John Doe",
                "number": "xxxxxxxxxxxx1234",
                "postal_code": "12345",
            },
            credit_limit="5000.00",
            currency_id="80000001-1234567890",
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                }
            ],
            customer_type_id="80000001-1234567890",
            email="customer@example.com",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            fax="+1-555-555-1212",
            first_name="John",
            is_active=True,
            job_description="Kitchen renovation project for residential client.",
            job_end_date=parse_date("2024-11-30"),
            job_projected_end_date=parse_date("2024-12-31"),
            job_start_date=parse_date("2024-01-15"),
            job_status="in_progress",
            job_title="Purchasing Manager",
            job_type_id="80000001-1234567890",
            last_name="Doe",
            middle_name="A.",
            note="Our favorite customer.",
            opening_balance="1000.00",
            opening_balance_date=parse_date("2023-01-01"),
            parent_id="80000001-1234567890",
            phone="+1-555-123-4567",
            preferred_delivery_method="email",
            preferred_payment_method_id="80000001-1234567890",
            price_level_id="80000001-1234567890",
            resale_number="123456789",
            sales_representative_id="80000001-1234567890",
            sales_tax_code_id="80000001-1234567890",
            sales_tax_country="us",
            sales_tax_item_id="80000001-1234567890",
            salutation="Dr.",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            tax_registration_number="GB123456789",
            terms_id="80000001-1234567890",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.customers.with_raw_response.create(
            name="Website Redesign Project",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.customers.with_streaming_response.create(
            name="Website Redesign Project",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.customers.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.customers.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.customers.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_contacts=[
                {
                    "id": "80000001-1234567890",
                    "revision_number": "1721172183",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-123-4567",
                        }
                    ],
                    "first_name": "John",
                    "job_title": "Purchasing Manager",
                    "last_name": "Doe",
                    "middle_name": "A.",
                    "salutation": "Dr.",
                }
            ],
            additional_notes=[
                {
                    "id": 1,
                    "note": "This is a fun note.",
                }
            ],
            alternate_contact="Bob Johnson",
            alternate_phone="+1-555-987-6543",
            alternate_shipping_addresses=[
                {
                    "name": "Alternate shipping address",
                    "city": "San Francisco",
                    "country": "United States",
                    "is_default_shipping_address": True,
                    "line1": "Conductor Labs Inc.",
                    "line2": "540 Market St.",
                    "line3": "Suite 100",
                    "line4": "",
                    "line5": "",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                }
            ],
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            cc_email="manager@example.com",
            class_id="80000001-1234567890",
            company_name="Acme Corporation",
            contact="Jane Smith",
            credit_card={
                "address": "1234 Main St, Anytown, USA, 12345",
                "expiration_month": 12,
                "expiration_year": 2024,
                "name": "John Doe",
                "number": "xxxxxxxxxxxx1234",
                "postal_code": "12345",
            },
            credit_limit="5000.00",
            currency_id="80000001-1234567890",
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                }
            ],
            customer_type_id="80000001-1234567890",
            email="customer@example.com",
            fax="+1-555-555-1212",
            first_name="John",
            is_active=True,
            job_description="Kitchen renovation project for residential client.",
            job_end_date=parse_date("2024-11-30"),
            job_projected_end_date=parse_date("2024-12-31"),
            job_start_date=parse_date("2024-01-15"),
            job_status="in_progress",
            job_title="Purchasing Manager",
            job_type_id="80000001-1234567890",
            last_name="Doe",
            middle_name="A.",
            name="Website Redesign Project",
            note="Our favorite customer.",
            parent_id="80000001-1234567890",
            phone="+1-555-123-4567",
            preferred_delivery_method="email",
            preferred_payment_method_id="80000001-1234567890",
            price_level_id="80000001-1234567890",
            resale_number="123456789",
            sales_representative_id="80000001-1234567890",
            sales_tax_code_id="80000001-1234567890",
            sales_tax_country="us",
            sales_tax_item_id="80000001-1234567890",
            salutation="Dr.",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            tax_registration_number="GB123456789",
            terms_id="80000001-1234567890",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.customers.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.customers.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.customers.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[Customer], customer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names=["ABC Corporation:Website Redesign Project"],
            ids=["80000001-1234567890"],
            limit=150,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            total_balance="123.45",
            total_balance_greater_than="123.45",
            total_balance_greater_than_or_equal_to="123.45",
            total_balance_less_than="123.45",
            total_balance_less_than_or_equal_to="123.45",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[Customer], customer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.customers.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(AsyncCursorPage[Customer], customer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.customers.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(AsyncCursorPage[Customer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True
