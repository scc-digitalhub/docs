# DBT runtime

The **DBT runtime** allows you to run [DBT](https://www.getdbt.com/) transformations on your data. It is a wrapper around the DBT CLI tool.

In a nutshell, DBT transformation in the platform aims at performing a simple transformation of a tabular data (e.g., data item) to another form using SQL-based operations, such as the one represented in the following example:

```sql
with customers as (

    select
        id as customer_id,
        first_name,
        last_name

    from {{ ref('customers') }}

),

orders as (

    select
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from {{ ref('shop_orders') }}

),

customer_orders as (

    select
        customer_id,

        min(order_date) as first_order_date,
        max(order_date) as most_recent_order_date,
        count(order_id) as number_of_orders

    from orders

    group by 1

),

final as (

    select
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        customer_orders.first_order_date,
        customer_orders.most_recent_order_date,
        coalesce(customer_orders.number_of_orders, 0) as number_of_orders

    from customers

    left join customer_orders using (customer_id)

)

select * from final
```

The DBT runtime function is defined with the SQL transformation code to be executed.

The only DBT action supported by the runtime is ``transform``, which 
takes references to the data items as inputs, applies the operation using the DBT executable, and creates resulting data item under the name defined in the output mapping.

The DBT transformation may be executed both in the platform and locally (provided DBT executable is available in your environment).

## Management with SDK

Check the [SDK DBT runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/dbt/overview/) for more information.
