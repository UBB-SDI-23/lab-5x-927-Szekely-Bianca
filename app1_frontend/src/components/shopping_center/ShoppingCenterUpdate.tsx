import { Button, Card, CardActions, CardContent, CircularProgress, Container, IconButton, TextField } from "@mui/material";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import {ShoppingCenter} from "../../models/ShoppingCenter";

import { BACKEND_API_URL } from "../../constants";

export const ShoppingCenterUpdate = () => {
    const navigate = useNavigate();
    const {ShoppingCenterId} = useParams();

    const [loading, setLoading] = useState(true);
    const [shop, setShoppingCenter] = useState({
        shop_name:"",
        shop_code:0,
        shop_category:"",
        nr_employee:0,
        shop_floor: 0,
    });

    useEffect(() => {
        const fetchShoppingCenter = async () => {
            const response = await fetch(`${BACKEND_API_URL}/ShoppingCenter/${ShoppingCenterId}/`);
            //const response = await fetch(`http://ec2-13-50-243-189.eu-north-1.compute.amazonaws.com:8000/app1/ShoppingCenter/${ShoppingCenterId}/`);
            const shop = await response.json();
            setShoppingCenter({
                shop_name: shop.shop_name,
                shop_code: shop.shop_code,
                shop_category: shop.shop_category,
                nr_employee: shop.nr_employee,
                shop_floor: shop.shop_floor
            })
            setLoading(false);
            console.log(shop);
        };
        fetchShoppingCenter();
    }, [ShoppingCenterId]);

    const updateShoppingCenter =async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            await axios.put(`${BACKEND_API_URL}/ShoppingCenter/${ShoppingCenterId}/`, shop);
            //await axios.put(`http://ec2-13-50-243-189.eu-north-1.compute.amazonaws.com:8000/app1/ShoppingCenter/${ShoppingCenterId}/`, shop);
            navigate(`/ShoppingCenter/${ShoppingCenterId}`);
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/tennisplayers`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<form onSubmit={updateShoppingCenter}>
                    <TextField
							id="shop_name"
							label="Shop name"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setShoppingCenter({ ...shop, shop_name: event.target.value })}
						/>
						<TextField
							id="shop_code"
							label="Unique Code"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setShoppingCenter({ ...shop, shop_code: Number(event.target.value) })}
						/>


                        <TextField
							id="shop_category"
							label="Category"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setShoppingCenter({ ...shop, shop_category: event.target.value })}
						/>

                        <TextField
							id="nr_employee"
							label="Number of employees"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setShoppingCenter({ ...shop, nr_employee: Number(event.target.value) })}
						/>

                        <TextField
							id="shop_floor"
							label="Shop Floor"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setShoppingCenter({ ...shop, shop_floor: Number(event.target.value) })}
						/>

						<Button type="submit">Update Shopping Center</Button>
					</form>
				</CardContent>
				<CardActions></CardActions>
			</Card>
		</Container>
    )
};