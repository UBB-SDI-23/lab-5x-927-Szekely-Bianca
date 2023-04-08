import { ShoppingCenter } from "./ShoppingCenter";

export interface Employee {
    id:number;
    employee_firstname:string;
    employee_lastname:string; 
    employee_salary:number; 
    employee_age:number;
    employee_phone:number;
    employee_shop:ShoppingCenter[];
}