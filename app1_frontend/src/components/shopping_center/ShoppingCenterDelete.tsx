import { Container, Card, CardContent, IconButton, CardActions, Button } from "@mui/material";
import { Link, useNavigate, useParams } from "react-router-dom";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { BACKEND_API_URL } from "../../constants";

export const ShoppingCenterDelete = () => {
    const {ShoppingCenterId} = useParams();
    const navigate = useNavigate();

    const handleDelete = async(event: {preventDefault: () => void}) => {
        event.preventDefault();
        //await axios.delete(`http://ec2-13-50-243-189.eu-north-1.compute.amazonaws.com:8000/app1/ShoppingCenter/${ShoppingCenterId}/`);
        await axios.delete(`${BACKEND_API_URL}/ShoppingCenter/${ShoppingCenterId}/`);
        navigate("/ShoppingCenter");
    };

    const handleCancel = (event: {preventDefault: () => void}) => {
        event.preventDefault();
        navigate("/ShoppingCenter");
    }

    return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/ShoppingCenter`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					Are you sure you want to delete this shop? This CANNOT be undone!
				</CardContent>
				<CardActions>
					<Button onClick={handleDelete}>Delete it</Button>
					<Button onClick={handleCancel}>Cancel</Button>
				</CardActions>
			</Card>
		</Container>
	);
}