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

import data from "./calendar.json";

class Calendarhorizontal extends React.Component {
  render() {
    Shape.registerShape("polygon", "boundary-polygon", {
      draw(cfg, container) {
        if (!Util.isEmpty(cfg.points)) {
          const attrs = {
            stroke: "#fff",
            lineWidth: 1,
            fill: cfg.color,
            fillOpacity: cfg.opacity
          };
          const points = cfg.points;
          const path = [
            ["M", points[0].x, points[0].y],
            ["L", points[1].x, points[1].y],
            ["L", points[2].x, points[2].y],
            ["L", points[3].x, points[3].y],
            ["Z"]
          ];
          attrs.path = this.parsePath(path);
          const polygon = container.addShape("path", {
            attrs
          });

          if (cfg.origin._origin.lastWeek) {
            const linePath = [
              ["M", points[2].x, points[2].y],
              ["L", points[3].x, points[3].y]
            ]; 

            container.addShape("path", {
              zIndex: 1,
              attrs: {
                path: this.parsePath(linePath),
                lineWidth: 1,
                stroke: "#404040"
              }
            });

            if (cfg.origin._origin.lastDay) {
              container.addShape("path", {
                zIndex: 1,
                attrs: {
                  path: this.parsePath([
                    ["M", points[1].x, points[1].y],
                    ["L", points[2].x, points[2].y]
                  ]),
                  lineWidth: 1,
                  stroke: "#404040"
                }
              });
            }
          }

          container.sort();
          return polygon;
        }
      }
    });
    const cols = {
      day: {
        type: "cat",
        values: [
          "Sun.",
          "Mon.",
          "Tue.",
          "Wed.",
          "Thu.",
          "Fri.",
          "Sat."
        ]
      },
      week: {
        type: "cat"
      },
      commits: {
        sync: true
      }
    };
    return (
      <div>
        <Chart
          height={window.innerHeight}
          data={data}
          scale={cols}
          forceFit
          padding={[window.innerHeight / 3, 20, window.innerHeight / 3, 80]}
        >
          <Tooltip title="launch" />
          <Axis
            name="week"
            position="top"
            tickLine={null}
            line={null}
            label={{
              offset: 12,
              textStyle: {
                fontSize: 12,
                fill: "#666",
                textBaseline: "top"
              },
              formatter: val => {
                if (val === "3") {
                  return "JAN";
                } else if (val === "7") {
                  return "FEB";
                } else if (val === "11") {
                  return "MAR";
                } else if (val === "18") {
                  return "APR";
                } else if (val === "21") {
                  return "MAY";
                } else if (val === "26") {
                  return "JUN";
                } else if (val === "32") {
                  return "JUL";
                } else if (val === "36") {
                  return "AUG";
                } else if (val === "39") {
                  return "SEP";
                } else if (val === "43") {
                  return "OCT";
                } else if (val === "47") {
                  return "NOV";
                } else if (val === "51") {
                  return "DEC";
                }

                return "";
              }
            }}
          />
          <Axis name="day" grid={null} />
          <Geom
            type="polygon"
            position="week*day*launch"
            shape="boundary-polygon"
            color={["release", "#BAE7FF-#1890FF-#0050B3"]}
          />
          <Coord reflect="y" />
        </Chart>
      </div>
    );
  }
}

export default Calendarhorizontal;