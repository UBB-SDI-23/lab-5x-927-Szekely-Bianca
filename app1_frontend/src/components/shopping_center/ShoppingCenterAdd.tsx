import { Button, Card, CardActions, CardContent, Container, IconButton, TextField } from "@mui/material";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { ShoppingCenter } from "../../models/ShoppingCenter";
import { BACKEND_API_URL } from "../../constants";

export const ShoppingCenterAdd = () => {
    const navigate = useNavigate();
    const [shop, setShoppingCenter] = useState({
        shop_name:"",
        shop_code:0,
        shop_category:"",
        nr_employee:0,
        shop_floor: 0,
    });

    const addShoppingCenter =async (event: { preventDefault: () => void}) => {
        event.preventDefault();
        try {
            await axios.post(`ec2-13-50-112-69.eu-north-1.compute.amazonaws.com:80/app1/ShoppingCenter/`, shop);
            //await axios.post(`${BACKEND_API_URL}/ShoppingCenter/`, shop);
            navigate("/ShoppingCenter");
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/ShoppingCenter`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<form onSubmit={addShoppingCenter}>
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

						<Button type="submit">Add Shopping Center</Button>
					</form>
				</CardContent>
				<CardActions></CardActions>
			</Card>
		</Container>
    );
}