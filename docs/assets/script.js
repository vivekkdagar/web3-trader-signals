// --- CONSTANTS ---
const CHART_COLORS = {
    red: 'var(--chart-red)',
    green: 'var(--chart-green)',
    blue: 'var(--chart-blue)',
    cyan: 'var(--chart-cyan)',
    pink: 'var(--chart-pink)',
    gray: '#A0AEC0',
    darkGray: '#6b7280',
};

// --- MOCK DATA GENERATION (Based on Analysis Insights) ---

// Mock data for 30 days
const mockDates = Array.from({ length: 30 }, (_, i) => {
    const date = new Date();
    date.setDate(date.getDate() - (30 - i));
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
});

const mockPnL = mockDates.map((_, i) => Math.random() * 100000 - 50000 + (i * 1000)); // Volatile but slightly upward
const mockSentimentNorm = mockDates.map((_, i) => (Math.sin(i / 5) * 0.2 + 0.6)); // Fluctuating between ~0.4 and ~0.8


// --- CHART 1: PnL vs Sentiment Time Series ---
function renderPnLSentimentChart() {
    const ctx = document.getElementById('pnlSentimentChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: mockDates,
            datasets: [
                {
                    label: 'Total PnL ($)',
                    data: mockPnL,
                    borderColor: CHART_COLORS.green,
                    backgroundColor: 'rgba(16, 185, 129, 0.2)',
                    yAxisID: 'yPnL',
                    tension: 0.3,
                    pointRadius: 3,
                    pointBackgroundColor: CHART_COLORS.green
                },
                {
                    label: 'Sentiment Index (0-1)',
                    data: mockSentimentNorm,
                    borderColor: CHART_COLORS.cyan,
                    backgroundColor: 'rgba(6, 182, 212, 0.2)',
                    yAxisID: 'ySentiment',
                    tension: 0.3,
                    pointRadius: 3,
                    pointBackgroundColor: CHART_COLORS.cyan
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: CHART_COLORS.gray, boxWidth: 10 } },
                tooltip: { mode: 'index', intersect: false }
            },
            scales: {
                x: { ticks: { color: CHART_COLORS.darkGray }, grid: { color: '#374151' } },
                yPnL: {
                    type: 'linear',
                    position: 'left',
                    title: { display: true, text: 'Total PnL ($)', color: CHART_COLORS.green },
                    ticks: { color: CHART_COLORS.darkGray, callback: (value) => value.toLocaleString('en-US') },
                    grid: { color: '#374151' }
                },
                ySentiment: {
                    type: 'linear',
                    position: 'right',
                    title: { display: true, text: 'Sentiment (0-1)', color: CHART_COLORS.cyan },
                    ticks: { color: CHART_COLORS.darkGray, min: 0, max: 1 },
                    grid: { drawOnChartArea: false }
                }
            }
        }
    });
}

// --- CHART 2: Trader Clustering Scatter Plot (Mocking 3D in 2D) ---
function renderClusteringChart() {
    // Mock data points (Volume vs PnL) colored by cluster
    const clusterData = [
        // Cluster 1: Risk Lover (High Volume, High PnL/Risk)
        { label: 'Risk Lover', color: CHART_COLORS.pink, count: 10, offset: 1.5 },
        // Cluster 2: Balanced Bob (Moderate)
        { label: 'Balanced Bob', color: CHART_COLORS.blue, count: 15, offset: 0.5 },
        // Cluster 3: Steady Eddy (Low PnL, Low Risk/Volume)
        { label: 'Steady Eddy', color: CHART_COLORS.cyan, count: 20, offset: 0 },
    ];

    const datasets = clusterData.map(cluster => {
        const dataPoints = Array.from({ length: cluster.count }, () => ({
            x: Math.random() * 50 + 50 * cluster.offset + 20, // Mock Volume (k units)
            y: (Math.random() * 50 - 25) + 50 * cluster.offset, // Mock PnL ($k)
        }));

        return {
            label: cluster.label,
            data: dataPoints,
            backgroundColor: cluster.color,
            pointRadius: 6,
            pointHoverRadius: 9,
            pointBorderColor: '#1f2937',
            pointBorderWidth: 2
        };
    });

    const ctx = document.getElementById('clusteringChart').getContext('2d');
    new Chart(ctx, {
        type: 'scatter',
        data: { datasets: datasets },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: CHART_COLORS.gray, usePointStyle: true } },
                tooltip: {
                    callbacks: {
                        label: (context) => `${context.dataset.label}: ($${context.parsed.y.toFixed(1)}k PnL, ${context.parsed.x.toFixed(1)}k Vol)`
                    }
                }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Total Volume (k units)', color: CHART_COLORS.gray },
                    ticks: { color: CHART_COLORS.darkGray },
                    grid: { color: '#374151' }
                },
                y: {
                    title: { display: true, text: 'Total PnL ($k)', color: CHART_COLORS.gray },
                    ticks: { color: CHART_COLORS.darkGray, callback: (value) => `$${value.toFixed(0)}k` },
                    grid: { color: '#374151' }
                }
            }
        }
    });
}

// --- CHART 3: Trade Side Distribution Pie Chart ---
function renderTradeSideChart() {
    const ctx = document.getElementById('tradeSideChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Buy (48.6%)', 'Sell (51.4%)'],
            datasets: [{
                data: [48.6, 51.4],
                backgroundColor: [CHART_COLORS.green, CHART_COLORS.red],
                borderColor: '#1f2937',
                borderWidth: 4,
                hoverOffset: 15
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom', labels: { color: CHART_COLORS.gray, boxWidth: 15, padding: 20 } },
                tooltip: { callbacks: { label: (context) => context.label } }
            },
            layout: { padding: 10 }
        }
    });
}

// --- CHART 4: Market Sentiment Gauge ---
function renderSentimentGaugeChart() {
    const sentimentScore = 51.2;
    const ctx = document.getElementById('sentimentGaugeChart').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Fear (0-49.9)', 'Neutral (50-59.9)', 'Greed (60-100)'],
            datasets: [{
                data: [49.9, 10, 40.1],
                backgroundColor: [CHART_COLORS.red, CHART_COLORS.blue, CHART_COLORS.green],
                borderWidth: 0,
            }]
        },
        options: {
            value: sentimentScore,
            responsive: true,
            maintainAspectRatio: false,
            rotation: 270,
            circumference: 180,
            cutout: '80%',
            plugins: {
                legend: { display: false },
                tooltip: { enabled: false }
            },
            layout: { padding: 20 }
        }
    });
    document.getElementById('sentimentValue').textContent = sentimentScore.toFixed(1);
}

// --- Initialization ---
window.onload = function () {
    // Register custom font for Tailwind
    tailwind.config = { theme: { extend: { fontFamily: { sans: ['Inter', 'sans-serif'] } } } };

    // Render all charts
    renderPnLSentimentChart();
    renderClusteringChart();
    renderTradeSideChart();
    renderSentimentGaugeChart();

    // Setup smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
};