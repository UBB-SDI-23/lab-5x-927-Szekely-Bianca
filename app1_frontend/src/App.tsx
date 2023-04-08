import { useState } from "react";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import * as React from "react";
import { AppBar, Toolbar, IconButton, Typography, Button } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppHome } from "./components/AppHome";
import { AppMenu } from "./components/AppMenu";
import { AllShoppingCenters } from "./components/shopping_center/ShoppingCenterShowAll";
import { ShoppingCenterDetails } from "./components/shopping_center/ShoppingCenterDetails";
import { ShoppingCenterAdd } from "./components/shopping_center/ShoppingCenterAdd";
import { ShoppingCenterDelete} from "./components/shopping_center/ShoppingCenterDelete";
import { ShoppingCenterUpdate } from "./components/shopping_center/ShoppingCenterUpdate";
import { ShoppingCenterAvgPriceProducts } from "./components/shopping_center/ShoppingCenterAvgPriceProducts";

function App() {
	return (
		<React.Fragment>
      <Box sx={{ minHeight: "100vh", backgroundColor: "#f0f0f0" }}>
			<Router>
				<AppMenu />

				<Routes>
					<Route path="/" element={<AppHome />} />
					<Route path="/ShoppingCenter" element={<AllShoppingCenters />} />
					<Route path="/ShoppingCenter/:ShoppingCenterId/" element={<ShoppingCenterDetails />} />
					<Route path="/ShoppingCenter/:ShoppingCenterId/edit" element={<ShoppingCenterUpdate />} />
					<Route path="/ShoppingCenter/:ShoppingCenterId/delete" element={<ShoppingCenterDelete />} />
					<Route path="/ShoppingCenter/add" element={<ShoppingCenterAdd />} /> 
					<Route path="/ShoppingCenter/AvgPriceProd" element={<ShoppingCenterAvgPriceProducts />} />
				</Routes>
			</Router>
      </Box>
		</React.Fragment>
	);
}

export default App;