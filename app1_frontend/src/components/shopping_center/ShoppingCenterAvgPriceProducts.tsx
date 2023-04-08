import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
} from "@mui/material";

import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ShoppingCenter } from "../../models/ShoppingCenter";
import {ShoppingCenterStats} from "../../models/ShoppingCenterStats";
import { BACKEND_API_URL } from "../../constants";


export const ShoppingCenterAvgPriceProducts = () => {
    const [loading, setLoading] = useState(true);
    const [shops, setShoppingCenter] = useState([]);

    useEffect(() => {
        fetch(`${BACKEND_API_URL}/ShoppingCenter/AveragePrice/`)
            .then(response => response.json())
            .then(data => {
                setShoppingCenter(data);
                setLoading(false);
            }
            );
    }, []);

    console.log(shops);

    return (
        <Container sx={{ color: "mediumorchid" }}>
        <h1>All the shops ordered by the average price of their products</h1>
        {loading && <CircularProgress />}

        {!loading && shops.length == 0 && <div>No shops found!</div>}

        {!loading && shops.length > 0 && (
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 900 }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>#</TableCell>
                            <TableCell align="right">Name</TableCell>
							<TableCell align="right">Unique Code</TableCell>
							<TableCell align="right">Category</TableCell>
							<TableCell align="right">Number of employees</TableCell>
                            <TableCell align="right">Floor</TableCell>
                            <TableCell align="center">Average price of products</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {shops.map((shop:ShoppingCenterStats, index) => (
                            <TableRow key={shop.id}>
                                <TableCell component="th" scope="row">
                                    {index + 1}
                                </TableCell>
                                <TableCell align="right">{shop.shop_name}</TableCell>
                                <TableCell align="right">{shop.shop_code}</TableCell>
								<TableCell align="right">{shop.shop_category}</TableCell>
								<TableCell align="right">{shop.nr_employee}</TableCell>
                                <TableCell align="right">{shop.shop_floor}</TableCell>
                                <TableCell align="center">{shop.avg_price}</TableCell>
                            </TableRow>
                        ))}
                </TableBody>
                </Table>
            </TableContainer>
        )}
    </Container>
    )
}