import { Card, CardActions, CardContent, IconButton } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { ShoppingCenter } from "../../models/ShoppingCenter";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";

export const ShoppingCenterDetails = () => {
	const { ShoppingCenterId } = useParams();
	const [shop, setShoppingCenter] = useState<ShoppingCenter>();

	useEffect(() => {
		const fetchShop = async () => {
			//const response = await fetch(`http://ec2-13-50-250-229.eu-north-1.compute.amazonaws.com/app1/ShoppingCenter/${ShoppingCenterId}/`);
            const response= await fetch(`${BACKEND_API_URL}/ShoppingCenter/${ShoppingCenterId}`)
			const shop = await response.json();
			setShoppingCenter(shop);
            console.log(shop);
		};
		fetchShop();
	}, [ShoppingCenterId]);

	return (
		<Container >
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/ShoppingCenter`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<h1 >Shopping Center Details</h1>
					<p> Name: {shop?.shop_name}</p>
                    <p>Unique Code: {shop?.shop_code}</p>
					<p>Category: {shop?.shop_category}</p>
					<p>Nr of employees: {shop?.nr_employee}</p>
					<p>Floor: {shop?.shop_floor}</p>
					<p>Employees:</p>
					<ul>
						{shop?.employees?.map((emp) => (
							<li key={emp.id}>{emp.employee_firstname} {emp.employee_lastname}</li>
						))}
					</ul>
					<p>Products:</p>
					<ul>
						{shop?.products?.map((product) => (
							<li key={product.id}>{product.product_name}</li>
						))}
					</ul>
				</CardContent>
				<CardActions>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/ShoppingCenter/${ShoppingCenterId}/edit`}>
						<EditIcon />
					</IconButton>

					<IconButton component={Link} sx={{ mr: 3 }} to={`/ShoppingCenter/${ShoppingCenterId}/delete`}>
						<DeleteForeverIcon sx={{ color: "red" }} />
					</IconButton>
				</CardActions>
			</Card>
		</Container>
	);
};