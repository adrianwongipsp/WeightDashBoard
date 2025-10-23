from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the test HTML file
        page.goto(f"file://{os.path.abspath('jules-scratch/verification/datos_test.html')}")

        # Wait for the charts to render
        page.wait_for_selector('#incrementBarChart rect')
        page.wait_for_selector('#lineChart circle')

        # Click on the bar in the "Incrementos por Sector de la Semana Actual" chart
        page.click('#incrementBarChart rect')

        # Wait for the popup to appear
        page.wait_for_selector('.popup-overlay', state='visible')

        # Take a screenshot
        page.screenshot(path='jules-scratch/verification/increment-chart-popup.png')

        # Close the popup
        page.click('.popup-close')

        # Click on a node in the "Evolución de Métricas en las Últimas 4 Semanas" chart
        page.click('#lineChart circle', force=True)

        # Wait for the popup to appear
        page.wait_for_selector('.popup-overlay', state='visible')

        # Take a screenshot
        page.screenshot(path='jules-scratch/verification/line-chart-popup.png')

        browser.close()

if __name__ == '__main__':
    run()
