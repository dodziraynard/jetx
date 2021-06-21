const canvas = document.getElementById('myChart')
const ctx = canvas?.getContext('2d');
const showStudentTeacherChart = (locations, buses) => {
    data = {
        labels: ['Location', 'Buses'],
        datasets: [{
            data: [locations, buses],
            backgroundColor: [
                'indigo',
                'orange',
            ],
        }],
    };
    if (ctx)
        new Chart(ctx, {
            type: 'doughnut',
            data: data,
        });
}

const values = canvas.dataset.values.split(",")
showStudentTeacherChart(...values)
