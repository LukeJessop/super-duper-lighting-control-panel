"use client";

import data from "@/data/data.json";
import { useState } from "react";
import PowerButton from "../Assets/SVG/power-off-solid.svg";
import PowerButtonGreen from "../Assets/SVG/power-off-solid-green.svg";
import Image from "next/image";
import { Axios } from "axios";

// const gridSquares = ["Config", ...data.scenes];

export default function Home() {
  const [lightsOn, setLightsOn] = useState(false);

  const toggleLightsRequest = () => {
    
  }

  return (
    <main className="flex ">
      <button onClick={() => setLightsOn(!lightsOn)}>
        <div className="p-4">
          <div className="w-12 h-12">
            {lightsOn ? (
              <Image alt="power-button" src={PowerButtonGreen} />
            ) : (
              <Image alt="power-button" src={PowerButton} />
            )}
          </div>
        </div>
      </button>
    </main>
  );
}
