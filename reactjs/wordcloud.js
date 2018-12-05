import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import {
  G2,
  Chart,
  Geom,
  Axis,
  Tooltip,
  Coord,
  Label,
  Legend,
  View,
  Guide,
  Shape,
  Facet,
  Util
} from "bizcharts";

import DataSet from "@antv/data-set";
import clouddata from "./wordcloud.json";
import _ from 'lodash';

//var _ = require('lodash');
//console.log("category")
class Wordcloud extends React.Component {
  render() {
    const colors = [
      /*'#FFF1B8', */
      "#E3F4BF",
      "#BEF7C8",
      "#86E6C8",
      "#36CFC9",
      "#209BDD",
      "#1581E6",
      "#0860BF"
    ];
    function getTextAttrs(cfg) {
      //cfg.color=colors;
      return _.assign(
        {},
        {
          fillOpacity: cfg.opacity,
          fontSize: cfg.origin._origin.size,
          rotate: cfg.origin._origin.rotate,
          text: cfg.origin._origin.text,
          textAlign: "center",
          fontFamily: cfg.origin._origin.font,
          fill: colors,
          textBaseline: "Alphabetic"
        },
        cfg.style
      );
    } 

    Shape.registerShape("point", "cloud", {
      drawShape(cfg, container) {
        const attrs = getTextAttrs(cfg);
        return container.addShape("text", {
          attrs: _.assign(attrs, {
            x: cfg.x,
            y: cfg.y
          })
        });
      }
    });
    const data = clouddata.data;
    const dv = new DataSet.View().source(data);
    const range = dv.range("size");
    const min = range[0];
    const max = range[1];
    //const color = dv.cfg.category;
    dv.transform({
      type: "tag-cloud",
      fields: ["genre", "size"],
      size: [window.innerWidth, window.innerHeight],
      font: "Verdana",
      padding: 0,
      timeInterval: 5000,

      // max execute time
      rotate() {
        let random = ~~(Math.random() * 4) % 4;

        if (random === 2) {
          random = 0;
        }

        return random * 90; // 0, 90, 270
      },

      fontSize(d) {
        if (d.value) {
          return ((d.value - min) / (max - min)) * (80 - 24) + 24;
        }

        return 0;
      }
    });
    const scale = {
      x: {
        nice: false
      },
      y: {
        nice: false
      }
    };
    return (
      <div>
        <Chart
          height={window.innerHeight}
          width={window.innerWidth}
          data={dv}
          scale={scale}
          padding={0}
          forceFit
        >
          <Tooltip showTitle={false} />
          <Coord reflect="y" />
          <Geom
            type="point"
            position="genre*y"
            //color={["category", colors]}
            shape="cloud"
            //tooltip="value*category"
            //color={["level", colors]}
          />
        </Chart>
      </div>
    );
  }
}

export default Wordcloud;





// class App extends Component {
//   render() {
//     return (
//       <div className="App">
//         <header className="App-header">
//           <img src={logo} className="App-logo" alt="logo" />
//           <p>
//             Edit <code>src/App.js</code> and save to reload.
//           </p>
//           <a
//             className="App-link"
//             href="https://reactjs.org"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             Learn React
//           </a>
//         </header>
//       </div>
//     );
//   }
// }

// export default App;
