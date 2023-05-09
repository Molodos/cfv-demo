function makeGraph(canvas, x, xLabel, y, yLabel, yMax, color, width) {
    const ctx = document.getElementById(canvas);
    new Chart(ctx, {
        type: "bar",
        data: {
            labels: x,
            datasets: [
                {
                    label: yLabel,
                    data: y,
                    backgroundColor: color,
                    barPercentage: width,
                    categoryPercentage: width
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: xLabel
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: yLabel
                    },
                    max: yMax
                }
            }
        }
    });
}
