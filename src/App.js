import React from "react";
import { render } from "react-dom";
import logo from "./logo.svg";
import "./App.css";
import * as d3 from "d3";
import data from "./data14.json";

class App extends React.Component {
  componentDidMount = () => {
    const svg = d3.select("svg");
    const width = 1900;
    const height = 1000;
    svg
      .append("defs")
      .selectAll("marker")
      .join("marker")
      .attr("id", `arrow`)
      .attr("viewBox", "0 -5 10 10")
      .attr("refX", 15)
      .attr("refY", -0.5)
      .attr("markerWidth", 6)
      .attr("markerHeight", 6)
      .attr("orient", "auto")
      .append("path")
      .attr("fill", "lightgray")
      .attr("d", "M0,-5L10,0L0,5");

    const nodes = data.nodes;
    const edges = data.edges;
    const simulation = d3
      .forceSimulation(nodes)
      .force("link", d3.forceLink(edges))
      .force("charge", d3.forceManyBody().strength(-35))
      .force("center", d3.forceCenter(width / 2, height / 2 + 10))
      .force("x", d3.forceX())
      .force("y", d3.forceY())
      .on("tick", ticked);
    // console.log(nodes, edges);
    const link = svg
      .append("g")
      .attr("fill", "none")
      .attr("stroke", "lightgray")
      .attr("stroke-width", 0.8)
      .selectAll("path")
      .data(edges)
      .join("path")
      // .attr("marker-end", `url(${new URL(`#arrow`)})`);

    const max = d3.max(nodes, (d) => d.weight);
    const min = d3.min(nodes, (d) => d.weight);
    const labels = {
      N2: 0,
      N3: 0,
      N4: 0,
      N5: 1,
      N6: 2,
      N7: 2,
      N8: 0,
      N9: 3,
      N10: 3,
      N11: 1,
      N12: 0,
      N13: 4,
      N14: 1,
      N15: 1,
      N16: 1,
      N17: 1,
      N18: 1,
      N19: 1,
      N20: 1,
      N21: 1,
      N22: 1,
      N23: 1,
      N24: 1,
      N25: 2,
      N26: 4,
      N27: 4,
      N28: 5,
      N32: 1,
      N33: 1,
      N34: 6,
      N35: 7,
      N36: 7,
      N41: 2,
      N42: 2,
      N45: 0,
      N46: 2,
      N47: 1,
      N48: 1,
      N49: 5,
      N50: 5,
      N51: 7,
      N52: 7,
      N53: 2,
      N56: 1,
      N57: 1,
      N58: 1,
      N59: 7,
      N60: 7,
      N61: 7,
      N62: 2,
      N63: 1,
      N72: 0,
      N73: 0,
      N74: 0,
      N77: 1,
      N78: 0,
      N79: 1,
      N81: 2,
      N82: 2,
      N83: 2,
      N84: 2,
      N85: 2,
      N86: 2,
      N87: 0,
      N88: 6,
      N89: 0,
      N90: 0,
      N91: 0,
      N92: 0,
      N93: 0,
      N94: 3,
      N95: 3,
      N96: 0,
      N97: 7,
      N98: 0,
      N99: 3,
      N100: 1,
      N102: 2,
      N103: 2,
      N106: 3,
      N107: 0,
      N111: 7,
      N112: 4,
      N113: 4,
      N115: 3,
      N118: 1,
      N121: 1,
      N122: 1,
      N132: 2,
      N133: 2,
      N134: 2,
      N136: 7,
      N140: 2,
      N145: 5,
      N146: 5,
      N147: 5,
      N148: 5,
      N149: 5,
      N150: 5,
      N151: 7,
      N152: 7,
      N153: 1,
      N158: 5,
      N159: 5,
      N160: 5,
      N161: 1,
      N162: 1,
      N163: 0,
      N164: 1,
      N175: 4,
      N176: 4,
      N177: 4,
      N179: 7,
      N180: 7,
      N181: 7,
      N183: 7,
      N184: 7,
      N185: 1,
      N186: 4,
      N192: 3,
      N193: 0,
      N194: 1,
      N195: 1,
      N197: 1,
      N205: 7,
      N206: 1,
      N213: 1,
      N214: 5,
      N215: 1,
      N220: 7,
      N221: 7,
      N231: 1,
      N234: 1,
      N236: 1,
      N241: 7,
      N244: 1,
      N245: 4,
      N246: 7,
      N247: 0,
      N249: 7,
      N250: 4,
      N252: 1,
      N253: 1,
      N254: 1,
      N257: 7,
      N258: 4,
      N259: 4,
      N260: 4,
      N261: 4,
      N262: 5,
      N263: 5,
      N264: 5,
      N265: 1,
      N266: 1,
      N267: 4,
      N268: 1,
      N273: 1,
      N274: 1,
      N275: 1,
      N279: 5,
      N280: 5,
      N281: 5,
      N282: 1,
      N283: 7,
      N284: 1,
      N287: 1,
      N288: 7,
      N289: 7,
      N290: 1,
      N291: 1,
      N292: 1,
      N295: 3,
      N296: 7,
      N307: 1,
      N308: 5,
      N309: 1,
      N313: 7,
      N314: 6,
      N315: 6,
      N316: 6,
      N317: 1,
      N318: 1,
      N319: 1,
      N320: 1,
      N321: 1,
      N324: 1,
      N325: 2,
      N326: 1,
      N327: 1,
      N328: 7,
      N329: 7,
      N332: 0,
      N335: 4,
      N336: 7,
      N337: 4,
      N338: 1,
      N339: 2,
      N340: 2,
      N341: 0,
      N342: 0,
      N343: 1,
      N344: 6,
      N345: 6,
      N346: 6,
      N347: 6,
      N348: 6,
      N349: 6,
      N350: 6,
      N351: 6,
      N352: 6,
      N353: 6,
      N354: 6,
      N355: 6,
      N356: 6,
      N357: 6,
      N358: 6,
      N359: 1,
      N360: 3,
      N361: 3,
      N362: 3,
      N363: 1,
      N364: 3,
      N365: 4,
      N366: 1,
      N367: 3,
      N368: 3,
      N371: 4,
      N372: 7,
      N373: 3,
      N374: 0,
      N375: 1,
      N376: 1,
      N377: 1,
      N378: 1,
      N379: 1,
      N380: 1,
      N381: 1,
      N382: 2,
      N383: 2,
      N384: 0,
      N385: 2,
      N386: 2,
      N387: 7,
      N388: 7,
      N389: 1,
      N390: 4,
      N391: 7,
      N392: 2,
      N393: 0,
      N394: 3,
      N395: 3,
      N396: 3,
      N397: 3,
      N398: 1,
      N399: 1,
      N400: 1,
      N401: 1,
      N402: 1,
      N403: 2,
      N404: 2,
      N405: 4,
      N406: 4,
      N407: 5,
      N408: 5,
      N409: 5,
      N410: 5,
      N411: 5,
      N412: 4,
      N413: 4,
      N414: 2,
      N415: 0,
      N416: 0,
      N417: 2,
      N418: 2,
      N419: 2,
      N420: 1,
      N421: 0,
      N422: 0,
      N423: 0,
      N424: 4,
      N425: 5,
      N426: 5,
      N427: 7,
      N428: 2,
      N429: 1,
      N430: 0,
      N431: 2,
      N432: 2,
      N433: 2,
      N434: 1,
      N435: 2,
      N436: 0,
      N437: 0,
      N438: 7,
      N439: 7,
      N440: 7,
      N441: 1,
      N442: 4,
      N443: 2,
      N444: 2,
      N445: 2,
    };
    const colors = [
      "#4e79a7",
      "#f28e2c",
      "#e15759",
      "#76b7b2",
      "#59a14f",
      "#edc949",
      "#af7aa1",
      "#ff9da7",
      "#9c755f",
      "#bab0ab",
    ];

    const node = svg
      .append("g")
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("fill", "steelblue")
      .attr("r", (d) => Math.sqrt(Math.sqrt(d.weight)) * 2)
      .on("mouseover", function (e, d) {
        d3.select(this).append("title").text(d.name);
      })
      .call(drag(simulation));

    function ticked() {
      // link
      //   .attr("x1", (d) => d.source.x)
      //   .attr("y1", (d) => d.source.y)
      //   .attr("x2", (d) => d.target.x)
      //   .attr("y2", (d) => d.target.y);
      link.attr("d", linkArc);
      node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
    }

    function drag(simulation) {
      function dragstarted(event) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
      }

      function dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
      }

      function dragended(event) {
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
      }

      return d3
        .drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
    }

    function linkArc(d) {
      const r = Math.hypot(d.target.x - d.source.x, d.target.y - d.source.y);
      return `
        M${d.source.x},${d.source.y}
        A${r},${r} 0 0,1 ${d.target.x},${d.target.y}
      `;
    }
  };
  render() {
    return (
      <div className="App">
        <svg style={{ height: 1000, width: 1900 }}></svg>
      </div>
    );
  }
}

export default App;
