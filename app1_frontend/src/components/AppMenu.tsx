import { Box, AppBar, Toolbar, IconButton, Typography, Button } from "@mui/material";
import { Link, useLocation } from "react-router-dom";
import StorefrontIcon from '@mui/icons-material/Storefront';
import LocalAtmIcon from '@mui/icons-material/LocalAtm';
import ShoppingBasketIcon from '@mui/icons-material/ShoppingBasket';

export const AppMenu = () => {
	const location = useLocation();
	const path = location.pathname;

	return (
		<Box sx={{ flexGrow: 1 }}>
			<AppBar position="static" sx={{ marginBottom: "20px" }} >
				<Toolbar sx={{ backgroundColor: "plum" }}>
					<IconButton
						component={Link}
						to="/"
						size="large"
						edge="start"
						color="inherit"
						aria-label="school"
						sx={{ mr: 2 }}>
						<StorefrontIcon />
					</IconButton>
					<Typography variant="h6" component="div" sx={{ mr: 5 }}>
						Shopping Center Management
					</Typography>
					<Button
						variant={path.startsWith("/ShoppingCenter") ? "outlined" : "text"}
						to="/ShoppingCenter"
						component={Link}
						color="inherit"
						sx={{ mr: 5 }}
						startIcon={<ShoppingBasketIcon />}>
						Shopping Center
					</Button>
					<Button
						variant={path.startsWith("/ShoppingCenter") ? "outlined" : "text"}
						to="/ShoppingCenter/AvgPriceProd"
						component={Link}
						color="inherit"
						sx={{ mr: 5 }}
						startIcon={<LocalAtmIcon />}>
						Average Price Products
					</Button>
				</Toolbar>
			</AppBar>
		</Box>
	);
};