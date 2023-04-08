import {ShoppingCenter} from "./ShoppingCenter"

export interface Product {
    id:number;
    product_name:string;
    product_price:number;
    product_pieces:number;
    product_color:string;
    shopping_center:ShoppingCenter[];
}