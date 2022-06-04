import React, { Component } from "react";
import Parvez from "../../images/parvez.jpg";
import Ruhanika from "../../images/ruhanika.jpg";
import "react-responsive-carousel/lib/styles/carousel.min.css"; 
import { Carousel } from "react-responsive-carousel";

function ModalView({image,heading}) {
  return (
    <div>
      <Carousel
        infiniteLoop={true}
        showArrows={true}
        autoPlay={true}
        showThumbs={true}
        showIndicators={true}
        showStatus={false}
        emulateTouch={true}
        showThumbs={false}
        swipeable={true}
        stopOnHover={true}
        interval={2000}
        transitionTime={500}
        thumbWidth= {100}
        swipeScrollTolerance={5}
        centerSlidePercentage = {50}
        dynamicHeight = {true}
        width = {'100%'}
      >
        <div className=" w-auto">
          <img
            src={image}
            className="rounded mx-auto d-block w-100"
           
            style={{
              borderRadius: "50%",
              border: "2px solid #fff",
              height: "350px",

            }}
          
          
          />
          <p className="legend">{heading}</p> 
       </div> 
        <div className=" w-auto"> 
          <img
            src={Parvez}
            className="rounded mx-auto d-block w-100"
           
            style={{
              borderRadius: "50%",
              border: "2px solid #fff",
              height: "350px",

            }}
          
          />
          <p className="legend">{heading}</p>
        </div>
       
      </Carousel>
    </div>
  );
}

export default ModalView;
