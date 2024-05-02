import D3blackbox from "d3blackbox";
import * as d3 from "d3";
const Barchart = D3blackbox(function(anchor, props) {
  var svg = d3.select(anchor.current),
    margin = { top: 0, right: 20, bottom: 30, left: 40 },
    width = props.width,
    height = props.height ;
    svg.selectAll("*").remove();

 var links=props.links;
 var nodes =props.nodes;
        
 var  width = props.width;
 var height = props.height ;
    
    function getNeighbors(node) {
      return links.reduce(function(neighbors, link) {
        if (link.target.id === node.id) {
          neighbors.push(link.source.id)
        } else if (link.source.id === node.id) {
          neighbors.push(link.target.id)
        }
        return neighbors
      }, [node.id])
    }
    
    function isNeighborLink(node, link) {
      return link.target.id === node.id || link.source.id === node.id
    }
    
    
    function getNodeColor(node, neighbors) {
      if (Array.isArray(neighbors) && neighbors.indexOf(node.id) > -1) {
        return node.level === 1 ? 'blue' : 'green'
      }
    
      return node.level === 1 ? 'red' : 'gray'
    }
    
    
    function getLinkColor(node, link) {
      return isNeighborLink(node, link) ? 'green' : '#E5E5E5'
    }
    
    function getTextColor(node, neighbors) {
      return Array.isArray(neighbors) && neighbors.indexOf(node.id) > -1 ? 'green' : 'black'
    }
    
   
    
    var circles = svg.selectAll(null)
      .data([80,125])
      .enter()
      .append("circle")
      .attr("cx", props.width/2)
      .attr("cy", props.height/2)
      .attr("r", d=>d)
      .style("fill", "none")
      .style("stroke", "#ccc");
    
    // simulation setup with all forces
    var linkForce = d3
      .forceLink()
      .id(function(link) {
     //   console.log(width,props.width)
        return link.id 
      }) .distance(10).strength(0.75);
    
     
    var attractForce = d3.forceManyBody().strength(-200).distanceMax(400).distanceMin(60);
    var repelForce = d3.forceManyBody().strength(-1*Math.sqrt(width*width+height*height)/8);
    
    var simulation = d3.forceSimulation().force('link', linkForce).force("repelForce",repelForce).force('radial', d3.forceRadial(function(d) {
        return d.level * 50
      }, width / 2, height / 2))
      .force('center', d3.forceCenter(width / 2, height / 2));
    
      
    var dragDrop = d3.drag().on('start', function(node) {
      node.fx = node.x
      node.fy = node.y
    }).on('drag', function(node) {
      simulation.alphaTarget(0.7).restart()
      node.fx = d3.event.x
      node.fy = d3.event.y
    }).on('end', function(node) {
      if (!d3.event.active) {
        simulation.alphaTarget(0)
      }
      node.fx = null
      node.fy = null
    })
    
    
    
    function selectNode(selectedNode) {
      var neighbors = getNeighbors(selectedNode)
    
      // we modify the styles to highlight selected nodes
      nodeElements.attr('fill', function(node) {
        return getNodeColor(node, neighbors) 
      })
      textElements.attr('fill', function(node) {
        return getTextColor(node, neighbors)
      })
      linkElements.attr('stroke', function(link) {
        return getLinkColor(selectedNode, link)
      })
    }
    
    var linkElements = svg.append("g")
      .attr("class", "links")
      .selectAll("line")
      .data(links)
      .enter().append("line")
      .attr("stroke-width", function(link) {
        return link.value;
      })
      .attr("stroke", "rgba(50, 50, 50, 0.2)")
     linkElements.attr("d", function(d) {
    
        // length of current path
        var pl = this.getTotalLength(),
          // radius of circle plus backoff
          r = (12) + 30, //<-- 12 is your radius 30 is the "back-off" distance
          // position close to where path intercepts circle
          m = this.getPointAtLength(pl - r);
    
        var dx = m.x - d.source.x,
          dy = m.y - d.source.y,
          dr = Math.sqrt(dx * dx + dy * dy);
    
        return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + m.x + "," + m.y;
      });
      
      
     
    var nodeElements = svg.append("g")
      .attr("class", "nodes")
      .selectAll("circle")
      .data(nodes)
      .enter().append("circle")
      .attr("r", 2)
      .attr("fill", getNodeColor)
      .call(dragDrop)
      .on('click', selectNode)
    
    var textElements = svg.append("g")
      .attr("class", "texts")
      .selectAll("text")
      .data(nodes)
      .enter().append("text")
      .text(function(node) {
        return node.label
      })
      .attr("font-size", 10)
      .attr("dx", 15)
      .attr("dy", 4)
    
    
    simulation
     .nodes(nodes)
     .on("tick", ticked)
    
    
    simulation.force("link")
     .links(links);
          
    function ticked() {
     nodeElements
        .attr('cx', function(node) {
          return node.x
        })
        .attr('cy', function(node) {
          return node.y
        })
      textElements
        .attr('x', function(node) {
          return node.x
        })
        .attr('y', function(node) {
          return node.y
        })
      linkElements
        .attr('x1', function(link) {
          return link.source.x
        })
        .attr('y1', function(link) {
          return link.source.y
        })
        .attr('x2', function(link) {
          return link.target.x
        })
        .attr('y2', function(link) {
          return link.target.y
        })
    } 
    
});


export default Barchart;