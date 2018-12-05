// data-set 可以按需引入，除此之外不要引入别的包
import React from 'react';
import { Chart, Axis, Tooltip, Geom, Coord, Legend } from 'bizcharts';
import DataSet from '@antv/data-set';
import dataset from './boxradial.json';

const { DataView } = DataSet;

const data = dataset.data;

const dv = new DataView().source(data);
dv.transform({
  type: 'map',
  callback: function callback(obj) {
    obj.range = [obj.low, obj.q1, obj.median, obj.q3, obj.high];
    return obj;
  },
});

class BoxRadial extends React.Component {
  render() {
    return (
      <Chart height={600} data={dv} forceFit>
        <Axis />
        <Legend />
        <Tooltip
          showTitle={false}
          itemTpl={'<li data-index={index} style="margin-bottom:4px;"><span style="background-color:{color};" class="g2-tooltip-marker"></span>{name}<br/><span style="padding-left: 16px">最大值：{high}</span><br/><span style="padding-left: 16px">上四分位数：{q3}</span><br/><span style="padding-left: 16px">中位数：{median}</span><br/><span style="padding-left: 16px">下四分位数：{q1}</span><br/><span style="padding-left: 16px">最小值：{low}</span><br/></li>'}
        />
        <Coord type="polar" innerRadius={0.5} />
        <Geom
          type="schema"
          position="month*range"
          size={60}
          shape="box"
          active
          color="month"
          tooltip={['month*low*q1*median*q3*high', (month, low, q1, median, q3, high) => ({
            name: month,
            low,
            q1,
            median,
            q3,
            high,
          })]}
        />
      </Chart>
    );
  }
}

export default BoxRadial;
