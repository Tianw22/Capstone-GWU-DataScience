import React from "react";
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

import data from "./donut.json";

function getComponent(data) {
  const dv = new DataSet.View().source(data);
  dv.transform({
    type: "fold",
    fields: ["<6", "6~7", "7~8","8~9",">9"],
    // 展开字段集
    key: "level",
    value: "count"
  }).transform({
    type: "percent",
    field: "count",
    dimension: "level",
    groupBy: ["month"],
    as: ["percent"]
  });

  class SliderChart extends React.Component {
    render() {
      return (
        <Chart height={window.innerHeight} data={dv} forceFit padding={0}>
          <Tooltip />
          <Facet
            type="list"
            cols={9}
            fields={["month"]}
            showTitle={false}
            padding={0}
            eachView={(view, facet) => {
              view.coord("theta", {
                radius: 0.8,
                innerRadius: 0.6
              });
              view
                .intervalStack()
                .position("percent")
                .color("level");
              view.guide().html({
                position: ["50%", "50%"],
                html:
                  '<div style="color:#8c8c8c;font-size: 14px;text-align: center;width: 10em;">' +
                  facet.data[0].month +
                  "</div>",
                alignX: "middle",
                alignY: "middle"
              });
            }}
          />
        </Chart>
      );
    }
  }
  return SliderChart;
}

class Piemultidonuts extends React.Component {
  render() {
    const SliderChart = getComponent(data);
    return (
      <div>
        <SliderChart />
      </div>
    );
  }
}

export default Piemultidonuts;
