import pandas as pd
import os

main_folder = os.path.dirname(__file__)
datasets_path = os.path.join(main_folder, "Datasets")

customers = pd.read_excel(rf"{datasets_path}\customers.xlsx",  sheet_name = 'Customers', parse_dates=["signup_date"])
regions = pd.read_excel(rf"{datasets_path}\regions.xlsx", sheet_name = 'Regions')
products = pd.read_excel(rf"{datasets_path}\products.xlsx", sheet_name = 'Products')
orders = pd.read_excel(rf"{datasets_path}\orders.xlsx", sheet_name = 'Orders', parse_dates=["order_date"])
order_items = pd.read_excel(rf"{datasets_path}\order_items.xlsx", sheet_name = 'Order_Items')
payments = pd.read_excel(rf"{datasets_path}\payments.xlsx", sheet_name = 'Payments', parse_dates=["payment_date"])

sales_df = (
    order_items
    .merge(orders, on="order_id", how="left")
    .merge(customers, on="customer_id", how="left")
    .merge(products, on="product_id", how="left")
    .merge(regions, on="region_id", how="left")
    .merge(payments, on="order_id", how="left")
)

sales_df["gross_sales"] = sales_df["price"] * sales_df["quantity"]
sales_df["discount_amount"] = sales_df["gross_sales"] * sales_df["discount"]
sales_df["net_sales"] = sales_df["gross_sales"] - sales_df["discount_amount"]


revenue_country_category = (
    sales_df
    .groupby(["country", "category"], as_index=False)
    .agg(
        total_revenue=("net_sales", "sum"),
        total_quantity=("quantity", "sum"),
        avg_discount=("discount", "mean")
    )
    .sort_values("total_revenue", ascending=False)
)

print(revenue_country_category.to_string(index=False))



top_customers = (
    sales_df
    .groupby(["customer_id", "customer_name"], as_index=False)
    .agg(lifetime_value=("net_sales", "sum"))
    .sort_values("lifetime_value", ascending=False)
)

print(top_customers.to_string(index=False))



high_value_orders = (
    sales_df
    .groupby("order_id", as_index=False)
    .agg(order_value=("net_sales", "sum"))
    .query("order_value > 3000")
)

print(high_value_orders.to_string(index=False))



unpaid_completed_orders = sales_df[
    (sales_df["order_status"] == "Completed") &
    (sales_df["payment_id"].isna())
][["order_id", "customer_name", "country", "net_sales"]].drop_duplicates()

print(unpaid_completed_orders.to_string(index=False))



sales_df["order_month"] = sales_df["order_date"].dt.to_period("M")

monthly_category_pivot = pd.pivot_table(
    sales_df,
    values="net_sales",
    index="order_month",
    columns="category",
    aggfunc="sum",
    fill_value=0
)

print(monthly_category_pivot)



payment_country_pivot = pd.pivot_table(
    sales_df,
    values="amount_paid",
    index="country",
    columns="payment_method",
    aggfunc="sum"
)

print(payment_country_pivot)



discount_analysis = (
    sales_df
    .groupby("category", as_index=False)
    .agg(
        gross_sales=("gross_sales", "sum"),
        discount_given=("discount_amount", "sum")
    )
)

discount_analysis["discount_pct"] = (
    discount_analysis["discount_given"] /
    discount_analysis["gross_sales"]
) * 100

discount_analysis.sort_values("discount_pct", ascending=False)

print(discount_analysis.to_string(index=False))




multi_category_customers = (
    sales_df
    .groupby("customer_id")["category"]
    .nunique()
    .reset_index(name="category_count")
    .query("category_count > 1")
)

print(multi_category_customers.to_string(index=False))




sales_df["age_group"] = pd.cut(
    sales_df["age"],
    bins=[18, 25, 35, 45, 55, 70],
    labels=["18-25", "26-35", "36-45", "46-55", "56+"]
)

aov_by_age = (
    sales_df
    .groupby("age_group", as_index=False, observed=True)
    .agg(avg_order_value=("net_sales", "mean"))
)

print(aov_by_age.to_string(index=False))