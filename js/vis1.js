class Vis1 {
    constructor(parentElement, data) {
        this.parentElement = parentElement;
        this.data = data;
        this.initVis();
    }

    initVis() {
        let vis = this;

        vis.margin = { top: 50, right: 20, bottom: 20, left: 20 };
        vis.width = document.getElementById(vis.parentElement).getBoundingClientRect().width - vis.margin.left - vis.margin.right;
        vis.height = document.getElementById(vis.parentElement).getBoundingClientRect().height - vis.margin.top - vis.margin.bottom;

        vis.svg = d3.select("#" + vis.parentElement)
            .append("svg")
            .attr("width", vis.width + vis.margin.left + vis.margin.right)
            .attr("height", vis.height + vis.margin.top + vis.margin.bottom)
            .append("g")
            .attr("transform", `translate(${vis.margin.left},${vis.margin.top})`);

        vis.title = vis.svg
            .append("text")
            .attr("class", "title")
            .attr("x", vis.width / 2)
            .attr("y", -30)
            .attr("text-anchor", "middle")
            .style("font-weight", "bold")
            .text("Smoking Status of People with Lung Cancer");

        vis.barChartGroup = vis.svg.append("g")
            .attr("class", "bar-chart")


        vis.xScale = d3.scaleBand()
            .range([0, vis.width])
            .padding(0.1);

        vis.yScale = d3.scaleLinear()
            .range([vis.height, 0]);

        vis.wrangleData();
    }

    wrangleData() {
        let vis = this;

        vis.currentSmoke = 0;
        vis.formerSmoke = 0;
        vis.neverSmoke = 0;

        vis.data.forEach(function(d) {
            if (d.Smoking_History === "Current Smoker") {
                vis.currentSmoke += 1;
            }
            if (d.Smoking_History === "Former Smoker") {
                vis.formerSmoke += 1;
            }
            if (d.Smoking_History === "Never Smoked") {
                vis.neverSmoke += 1;
            }
        });

        vis.smokeStatus = [
            { type: "Never Smoked", count: vis.neverSmoke },
            { type: "Former Smoker", count: vis.formerSmoke },
            { type: "Current Smoker", count: vis.currentSmoke },
        ];

        console.log(vis.smokeStatus);
        vis.updateVis();
    }

    updateVis() {
        let vis = this;


        vis.xScale.domain(vis.smokeStatus.map(d => d.type));
        vis.yScale.domain([0, d3.max(vis.smokeStatus, d => d.count)]);

        vis.barChartGroup.selectAll("rect")
            .data(vis.smokeStatus)
            .enter()
            .append("rect")
            .attr("class", "bar")
            .attr("x", d => vis.xScale(d.type))
            .attr("y", d => vis.yScale(d.count))
            .attr("width", vis.xScale.bandwidth())
            .attr("height", d => vis.height - vis.yScale(d.count))
            .attr("fill", d => {
                if (d.type === "Never Smoked") return "#b0bfc9";
                if (d.type === "Former Smoker") return "#a66249";
                if (d.type === "Current Smoker") return "#ee5f2c";
            });

        vis.barChartGroup.selectAll(".bar-text")
            .data(vis.smokeStatus)
            .enter()
            .append("text")
            .attr("class", "bar-text")
            .attr("x", d => vis.xScale(d.type) + vis.xScale.bandwidth() / 2)
            .attr("y", d => vis.yScale(d.count) - 5)
            .attr("text-anchor", "middle")
            .text(d => d.count);

        vis.barChartGroup.append("g")
            .attr("class", "x-axis")
            .attr("transform", "translate(0," + vis.height + ")")
            .call(d3.axisBottom(vis.xScale));
    }
}
