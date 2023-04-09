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
	Button,
} from "@mui/material";
import React from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { BACKEND_API_URL } from '../../constants';
import { ShoppingCenter } from "../../models/ShoppingCenter";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import InfoIcon from '@mui/icons-material/Info';
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import { ShoppingCenterDetails } from "./ShoppingCenterDetails";

export const AllShoppingCenters = () => {
	const [loading, setLoading] = useState(false);
	//const [loading, setLoading] = useState(true);
	const [shops, setShoppingCenter] = useState<ShoppingCenter[]>([]);
	//const [shops, setShoppingCenter] = useState([])

	useEffect(() => {
		setLoading(true);
		//fetch(`http://ec2-13-50-250-229.eu-north-1.compute.amazonaws.com/app1/ShoppingCenter/`)
        fetch(`${BACKEND_API_URL}/ShoppingCenter/`)
			.then((response) => response.json())
			.then((data) => {
				setShoppingCenter(data);
				setLoading(false);
			});
	}, []);

	 console.log(shops);

    const sortShops = () => {
        const sorted= [...shops].sort((a: ShoppingCenter, b:ShoppingCenter) => {
            if (a.shop_floor < b.shop_floor) {
                return -1;
            }
            if (a.shop_floor > b.shop_floor) {
                return 1;
            }
            return 0;

        })
        console.log(sorted);
        setShoppingCenter(sorted);
    }


	return (
		<Container sx={{ color: "mediumorchid" }}>
			<h1>All Shops</h1>

			{loading && <CircularProgress />}
			{!loading && shops.length === 0 && <p>No shops found</p>}
			{!loading && (
				<IconButton component={Link} sx={{ mr: 3 }} to={`/ShoppingCenter/add`}>
					<Tooltip title="Add a new shop" arrow>
						<AddIcon color="primary" />
					</Tooltip>
				</IconButton>
			)}

			{!loading && (
            <Button color="primary" onClick={sortShops}>
                Sort shops by floor
            </Button>
        	)}

			{!loading && shops.length > 0 && (
				<TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell>#</TableCell>
                                <TableCell align="right">Name</TableCell>
								<TableCell align="right">Unique Code</TableCell>
								<TableCell align="right">Category</TableCell>
								<TableCell align="right">Number of employees</TableCell>
                                <TableCell align="right">Floor</TableCell>
								<TableCell align="center">Operations</TableCell>
							</TableRow>
						</TableHead>
						<TableBody>
							{shops.map((ShoppingCenter, index) => (
								<TableRow key={ShoppingCenter.id}>
									<TableCell component="th" scope="row">
										{index + 1}
									</TableCell>
									<TableCell component="th" scope="row">
										<Link to={`/ShoppingCenter/${ShoppingCenter.id}`} title="View shopping center details">
											{ShoppingCenter.shop_name}
										</Link>
									</TableCell>
                                    <TableCell align="right">{ShoppingCenter.shop_code}</TableCell>
									<TableCell align="right">{ShoppingCenter.shop_category}</TableCell>
									<TableCell align="right">{ShoppingCenter.nr_employee}</TableCell>
                                    <TableCell align="right">{ShoppingCenter.shop_floor}</TableCell>
									<TableCell align="right">
										<IconButton
											component={Link}
											sx={{ mr: 3 }}
											to={`/ShoppingCenter/${ShoppingCenter.id}`}>
											<Tooltip title="View shopping center details" arrow>
												<ReadMoreIcon color="primary" />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/ShoppingCenter/${ShoppingCenter.id}/edit`}>
											<Tooltip title="Edit shop details" arrow>
												<EditIcon />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/ShoppingCenter/${ShoppingCenter.id}/delete`}>
											<Tooltip title="Delete shop" arrow>
												<DeleteForeverIcon sx={{ color: "red" }} />
											</Tooltip>
										</IconButton>
									</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			)}
		</Container>
	);
};