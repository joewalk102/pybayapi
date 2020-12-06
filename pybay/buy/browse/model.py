from marshmallow import fields
from models import CamelCaseSchema


class Image(CamelCaseSchema):
    height = fields.Integer()
    image_url = fields.String()
    width = fields.Integer()


class Category(CamelCaseSchema):
    category_id = fields.String()


class CompatibilityProperties(CamelCaseSchema):
    localized_name = fields.String()
    name = fields.String()
    value = fields.String()


class Location(CamelCaseSchema):
    address_line_1 = fields.String()
    address_line_2 = fields.String()
    city = fields.String()
    country = fields.String()
    county = fields.String()
    postal_code = fields.String()
    state_or_providence = fields.String()


class Price(CamelCaseSchema):
    converted_from_currency = fields.String()
    converted_from_value = fields.String()
    currency = fields.String()
    value = fields.String()


class MarketingPrice(CamelCaseSchema):
    discount_amount = fields.Nested(Price)
    discount_percentage = fields.String()
    original_price = fields.Nested(Price)
    price_treatment = fields.String()


class Distance(CamelCaseSchema):
    unit_of_measure = fields.String()
    value = fields.String()


class PickupOptions(CamelCaseSchema):
    pickup_location_type = fields.String()


class Seller(CamelCaseSchema):
    feedback_percentage = fields.String()
    feedback_score = fields.Integer()
    seller_account_type = fields.String()
    username = fields.String()


class ShippingOption(CamelCaseSchema):
    guaranteed_delivery = fields.Boolean()
    max_estimated_delivery_date = fields.String()
    min_estimated_delivery_date = fields.String()
    shipping_cost = fields.Nested(Price)
    shipping_cost_type = fields.String()


class ItemSummary(CamelCaseSchema):
    additional_images = fields.List(fields.Nested(Image))
    adult_only = fields.Boolean()
    available_coupons = fields.Boolean()
    bid_count = fields.Integer()
    buying_options = fields.List(fields.String())
    categories = fields.List(fields.Nested(Category))
    compatibility_match = fields.String()
    compatibility_properties = fields.List(fields.Nested(CompatibilityProperties))
    condition = fields.String()
    condition_id = fields.String()
    current_bid_price = fields.Nested(Price)
    distance_from_pickup_location = fields.Nested(Distance)
    energy_efficiency_class = fields.String()
    epid = fields.String()
    image = fields.Nested(Image)
    item_affiliate_web_url = fields.String()
    item_group_href = fields.String()
    item_group_type = fields.String()
    item_href = fields.String()
    item_id = fields.String()
    item_location = fields.Nested(Location)
    item_web_url = fields.String()
    legacy_item_id = fields.String()
    marketing_price = fields.Nested(MarketingPrice)
    pickup_options = fields.Nested(PickupOptions)
    price = fields.Nested(Price)
    price_display_condition = fields.String()
    qualified_programs = fields.List(fields.String())
    seller = fields.Nested(Seller)
    shipping_options = fields.List(fields.Nested(ShippingOption))
    short_description = fields.String()
    thumbnail_images = fields.List(fields.Nested(image))
    title = fields.String()
    unit_price = fields.Nested(Price)
    unit_pricing_measure = fields.String()


class Corrections(CamelCaseSchema):
    q = fields.String()


class AspectDistribution(CamelCaseSchema):
    localized_aaspect_value = fields.String()
    match_count = fields.Integer()
    refinement_href = fields.String()


class AspectDistributions(CamelCaseSchema):
    aspect_value_distributions = fields.List(fields.Nested(AspectDistribution))


class BuyingOptionDistribution(CamelCaseSchema):
    buying_option = fields.String()
    match_count = fields.Integer()
    refinement_href = fields.String()


class CategoryDistributions(CamelCaseSchema):
    category_id = fields.String()
    category_name = fields.String()
    match_count = fields.Integer()
    refinement_href = fields.String()


class ConditionDistributions(CamelCaseSchema):
    condition = fields.String()
    condition_id = fields.String()
    match_count = fields.Integer()
    refinement_href = fields.String()


class Refinement(CamelCaseSchema):
    aspect_distributions = fields.List(fields.Nested(AspectDistributions))
    buying_option_distributions = fields.List(fields.Nested(BuyingOptionDistribution))
    category_distributions = fields.List(fields.Nested(CategoryDistributions))
    condition_distributions = fields.List(fields.Nested(ConditionDistributions))
    dominant_category_id = fields.String()


class NameValuePair(CamelCaseSchema):
    name = fields.String()
    value = fields.String()


class APIWarning(CamelCaseSchema):
    category = fields.String()
    domain = fields.String()
    error_id = fields.Integer()
    input_ref_ids = fields.List(fields.String())
    long_message = fields.String()
    message = fields.String()
    output_ref_ids = fields.List(fields.String())
    parameters = fields.List(fields.Nested(NameValuePair))
    subdomain = fields.String()


class SearchResults(CamelCaseSchema):
    auto_corrections = fields.Nested(Corrections)
    href = fields.String()
    item_summaries = fields.List(fields.Nested(ItemSummary))
    limit = fields.Integer()
    next = fields.String()
    offset = fields.Integer()
    prev = fields.String()
    refinement = fields.Nested(Refinement)
    total = fields.Integer()
    warnings = fields.List(fields.Nested(APIWarning))
