# Product Management API

This API allows you to manage products in a system. It supports operations like creating, updating, retrieving, and deleting products. The API is built using FastAPI.

## Table of Contents
- [Overview](#overview)
- [Endpoints](#endpoints)
  - [Create Product](#create-product)
  - [Get Product](#get-product)
  - [Update Product](#update-product)
  - [Delete Product](#delete-product)
- [Usage](#usage)
  - [Making Requests](#making-requests)
  - [Request Body Formats](#request-body-formats)
- [Error Handling](#error-handling)
  
## Overview

The Product Management API allows you to perform CRUD operations on products. Each product has the following fields:
- `name`: Name of the product
- `category`: Category of the product
- `description`: A detailed description of the product
- `product_image`: URL of the product image
- `sku`: Stock Keeping Unit identifier for the product
- `unit_of_measure`: The unit of measurement for the product (e.g., piece, kg)
- `lead_time`: Time in days it takes to ship the product
- `created_date`: Date when the product was created
- `updated_date`: Date when the product was last updated

## Endpoints

### 1. Create Product
**Endpoint**: `POST /product/create`

**Description**: This endpoint creates a new product.

**Request Body Example**:

```json
{
  "name": "Product Name",
  "category": "Electronics",
  "description": "High quality electronics.",
  "product_image": "http://example.com/product-image.jpg",
  "sku": "SKU12345",
  "unit_of_measure": "piece",
  "lead_time": 5
}
```

### 2. Get Product by ID
**Endpoint**: `GET /product/{pid}`

**Description**: This endpoint retrieves a product by its unique ID.

**Request Parameters**:
- `pid`: The product ID (integer).

**Response Example**:

```json
{
  "id": 1,
  "name": "Product Name",
  "category": "Electronics",
  "description": "High quality electronics.",
  "product_image": "http://example.com/product-image.jpg",
  "sku": "SKU12345",
  "unit_of_measure": "piece",
  "lead_time": 5,
  "created_date": "2024-12-12T00:00:00",
  "updated_date": "2024-12-12T00:00:00"
}
```



### 3. Update Product
**Endpoint**: `PUT /product/{pid}/update`

**Description**: This endpoint updates an existing product by its unique ID. You can update one or more fields of the product.

**Request Parameters**:
- `pid`: The product ID (integer).

**Request Body Example**:

```json
{
  "name": "Updated Product Name",
  "category": "Electronics",
  "description": "Updated description for high quality electronics.",
  "product_image": "http://example.com/updated-product-image.jpg",
  "sku": "SKU12345",
  "unit_of_measure": "piece",
  "lead_time": 7
}
```

### 4. List all Products
**Endpoint**: `GET /product/product/list`

**Description**: This endpoint Lists All Products 


**Response Example**:

```json
[
  {
    "name": "Test34324242",
    "category": "finished",
    "description": "This is a test product",
    "product_image": "http://example.com/image.jpg",
    "sku": "34343",
    "unit_of_measure": "unit",
    "lead_time": 10,
    "id": 1,
    "created_date": "2024-12-12T10:42:09",
    "updated_date": "2024-12-12T10:51:40"
  },
  {
    "name": "Test 1",
    "category": "semi-finished",
    "description": "This is a test product",
    "product_image": "http://example.com/image.jpg",
    "sku": "SKU12335",
    "unit_of_measure": "unit",
    "lead_time": 10,
    "id": 8,
    "created_date": "2024-12-12T10:48:39",
    "updated_date": "2024-12-12T10:48:39"
  },
  {
    "name": "Test 1",
    "category": "semi-finished",
    "description": "This is a test product",
    "product_image": "http://example.com/image.jpg",
    "sku": "SKU123335",
    "unit_of_measure": "unit",
    "lead_time": 10,
    "id": 9,
    "created_date": "2024-12-12T10:49:10",
    "updated_date": "2024-12-12T10:49:10"
  }
]
```


