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
    const labels = [
      4, 4, 0, 0, 4, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 3, 3, 3, 0, 4, 4, 0, 0, 3, 3, 3, 3, 0, 0, 3, 3, 0, 0, 0, 4, 0,
      0, 5, 5, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 7, 7, 3, 3, 4, 4, 4,
      3, 7, 0, 4, 4, 3, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 2, 0, 0, 0, 0, 2,
      0, 3, 0, 0, 3, 7, 0, 0, 7, 7, 7, 5, 0, 0, 7, 2, 1, 1, 0, 4, 4, 0, 0, 7, 7,
      4, 4, 4, 3, 7, 1, 1, 0, 0, 0, 7, 0, 1, 1, 7, 0, 3, 7, 1, 1, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 7, 7, 1, 1, 0, 0, 0, 0, 0, 0, 0, 7, 3, 3, 3, 4, 4, 7, 4, 7, 7,
      4, 0, 4, 7, 0, 0, 0, 7, 0, 0, 0, 0, 7, 7, 7, 7, 7, 2, 0, 0, 0, 7, 0, 3, 3,
      7, 7, 7, 7, 7, 0, 0, 3, 3, 7, 3, 7, 7, 0, 0, 0, 7, 7, 7, 7, 5, 5, 1, 1, 7,
      7, 7, 7, 7, 7, 7, 0, 3, 3, 0, 3, 0, 1, 3, 3, 1, 0, 1, 1, 0, 0, 5, 0, 3, 0,
      0, 4, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
      0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 3, 3, 4,
      4, 4, 4, 4, 3, 1, 1, 0, 4, 0, 3, 3, 3, 0, 4, 4, 4, 0, 0, 0, 0, 0, 4, 4, 0,
      0, 0, 0, 0, 0, 3, 3, 0, 7, 7, 0, 0, 0, 0, 0, 0, 4, 4, 0, 4, 4, 4, 4, 4, 4,
      4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 2, 2, 2, 0, 2, 0, 0, 2, 2, 7, 7, 0, 0, 2, 4,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 6, 6,
      6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ];

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
      // .attr("stroke", "lightgray")
      .attr("stroke-width", 0.8)
      .selectAll("path")
      .data(edges)
      .join("path");
    // .attr("marker-end", `url(${new URL(`#arrow`)})`);

    const max = d3.max(nodes, (d) => d.weight);
    const min = d3.min(nodes, (d) => d.weight);
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
      // .attr("fill", "steelblue")
      .attr("fill", (_, i) => {
        return colors[labels[i]];
      })
      // .attr("r", 2.5)
      .attr("r", (d) => Math.sqrt(Math.sqrt(d.weight)) * 2)
      .on("mouseover", function (e, d) {
        d3.select(this).append("title").text(d.name);
        d3.selectAll("path").attr("opacity", (dd, ii) => {
          if (dd.source === d || dd.target === d) {
            return 1;
          } else return 0.05;
        });
      })
      .on("mouseout", () => {
        d3.selectAll("path").attr("opacity", 1);
      })
      .call(drag(simulation));

    const text = svg
      .selectAll(".text")
      .data(nodes)
      .join("text")
      .attr("font-size", "4")
      .attr("stroke", "gray")
      .attr("stroke-width", 0.2)
      .text((d) => (d.weight > 1 ? d.name : ""));

    function ticked() {
      link.attr("d", linkArc).attr("stroke", (d) => {
        return "lightgray";
        // return kernel_4_edges.indexOf(
        //   (d.source.id, d.target.id)
        // ) !== -1
        //   ? "darkorange"
        //   : "lightgray";
      });
      node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
      text.attr("x", (d) => d.x).attr("y", (d) => d.y);
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
