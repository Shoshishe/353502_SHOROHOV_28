const data = Array.from({ length: 100 }, (_, index) => 1 / (index + 1));
const eps = 0.01

const animation = {
    x: {
        title: {
            display: true,
            text: "Value of argument"
        },
        type: 'number',
        easing: 'linear',
        duration: 10000 / data.length,
        from: NaN,
        delay(ctx) {
            if (ctx.type !== 'data' || ctx.xStarted) {
                return 0;
            }
            ctx.xStarted = true;
            return ctx.index * 10000 / data.length;
        }
    },
    y: {
        title: {
            display: true,
            text: "Value of function"
        },
        type: 'number',
        easing: 'linear',
        duration: 10000 / data.length,
        from: 0,
        delay(ctx) {
            if (ctx.type !== 'data' || ctx.yStarted) {
                return 0;
            }
            ctx.yStarted = true;
            return ctx.index * 10000 / data.length;
        }
    }
}

new Chart(
    document.getElementById('acquisitions'),
    {
        type: 'line',
        data: {
            labels: data.map((row, index) => index),
            datasets: [
                {
                    label: 'Real function',
                    data: data.map((row) => Math.log(1 - row))
                },
                {
                    label: 'Taylor series approx',
                    data: data.map((row) => {
                        let sum = 0;
                        let i = 1;
                        while (Math.abs(Math.pow(-1, i) * Math.pow(row, i) / i) >= eps) {
                            sum += Math.pow(-1, i) * Math.pow(row, i) / i;
                            i++;
                        }
                        return sum;
                    })
                }
            ],
        },
        options: {
            animation
        }
    }
);