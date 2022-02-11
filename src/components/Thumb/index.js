import React from 'react';
// Styles
import { Image } from './Thumb.styles';
import {usePurchase} from "../../hooks/usePurchase";
import Button from "../Button";


const Thumb = ({ image, eventName, artistName, date, genre, price, eid, soldout, city, location }) => {
        const { setIsPurchasing, setEid } = usePurchase();
        return(
            <div>
                <Image src={image} alt='artist-Thumb'/>
                <h3>{eventName}</h3>
                <h3>{artistName}</h3>
                <h3>{city}</h3>
                <h3>{location}</h3>
                <h4>{date}</h4>
                <h4>{genre}</h4>
                <h3>{price} PLN</h3>
                {soldout == 0 ?
                    <Button text={'Buy ticket'} callback={() => {setIsPurchasing(true); setEid(eid)}}/> :
                    <h4>sold out!</h4>
                }

            </div>
        )
};

export default Thumb;