import { Employee } from "./Employee";
import { Product } from "./Product";

export interface ShoppingCenter {
    id?:number;
    shop_code:number;
    shop_name:string;
    shop_category:string;
    nr_employee:number;
    shop_floor: number;
    //products:number[];
    products?:Product[];
    employees?:Employee[];
}