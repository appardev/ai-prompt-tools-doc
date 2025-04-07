# Tool key: foodai-tools, version: 4

# Tool key: foodai-tools, version: 3

[
    {
        "type": "function",
        "function": {
            "name": "add_food_to_cart",
            "description": "將食物加入到購物車中",
            "parameters": {
                "type": "object",
                "properties": {
                    "food_name": {
                        "type": "string",
                        "description": "食物名稱"
                    },
                    "unit_price": {
                        "type": "number", 
                        "description": "食物單價"
                    },
                    "quantity": {
                        "type": "integer",
                        "description": "新增的該品項的數量, 例如 1, 2, 3"
                    },
                    "remark": {
                        "type": "string",
                        "description": "食物備註"
                    }
                },
                "required": ["food_name", "unit_price", "quantity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "remove_food_from_cart",
            "description": "將食物從購物車中移除",
            "parameters": {
                "type": "object",
                "properties": {
                    "food_name": {
                        "type": "string",
                        "description": "食物名稱"
                    },
                    "quantity": {
                        "type": "integer",
                        "description": "移除的該品項的數量, 例如 1, 2, 3"
                    }
                },
                "required": ["food_name", "quantity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_food_remark",
            "description": "更新食物的備註",
            "parameters": {
                "type": "object",
                "properties": {
                    "food_name": {
                        "type": "string",
                        "description": "食物名稱"
                    },
                    "remark": {
                        "type": "string",
                        "description": "食物備註"
                    }
                },
                "required": ["food_name", "remark"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "submit_cart",
            "description": "送出訂單，一般點菜不需要直接送出訂單，只有在顧客很明確指出要提交訂單時，才會呼叫此工具。",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "switch_language",
            "description": "切換語言",
            "parameters": {
                "type": "object",
                "properties": {
                    "language": {
                        "type": "string",
                        "description": "語言",
                        "enum": ["zh_hant", "zh_hans", "en", "ja"]
                    }
                },
                "required": ["language"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_cart_all_items",
            "description": "確認購物車內容，此工具會回傳購物車內項目的列表",
            "parameters": {}
        }
    },
]
