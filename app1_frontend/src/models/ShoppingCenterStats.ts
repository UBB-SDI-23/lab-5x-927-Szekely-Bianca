import {Product} from "./Product";

export interface ShoppingCenterStats {
    id:number;
    shop_code:number;
    shop_name:string;
    shop_category:string;
    nr_employee:number;
    shop_floor: number;
    //products:number[];
    products:Product[];
    avg_price:number;
}