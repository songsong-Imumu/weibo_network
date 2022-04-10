import React from "react";
import { render } from "react-dom";
import logo from "./logo.svg";
import "./App.css";
import * as d3 from "d3";
import data from "./data9.json";

class App extends React.Component {
  componentDidMount = () => {
    const svg = d3.select("svg");
    const width = 1900;
    const height = 1000;
    const nodes = data.nodes;
    const edges = data.edges;
    const simulation = d3
      .forceSimulation(nodes)
      .force("link", d3.forceLink(edges))
      .force("charge", d3.forceManyBody().strength(-60))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("x", d3.forceX())
      .force("y", d3.forceY())
      .on("tick", ticked);
    // console.log(nodes, edges);
    const link = svg
      .append("g")
      .attr("stroke", "lightgray")
      .attr("stroke-width", 1)
      .selectAll("line")
      .data(edges)
      .join("line");

    const node = svg
      .append("g")
      .attr("fill", "steelblue")
      .attr("stroke", "white")
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("r", 4)
      .attr("opacity", (d) => (d.name === "" ? 0 : 1))
      .on("mouseover", function (e, d) {
        d3.select(this).append("title").text(d.name);
      })
      .call(drag(simulation));

    function ticked() {
      link
        .attr("x1", (d) => d.source.x)
        .attr("y1", (d) => d.source.y)
        .attr("x2", (d) => d.target.x)
        .attr("y2", (d) => d.target.y);

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
