"""Use installed Playwright + Chromium; reads only local HTML, writes local screenshots."""
from pathlib import Path
from tempfile import mkdtemp
from playwright.sync_api import sync_playwright

repo=Path(__file__).resolve().parents[2]
html_path=repo/'semesters/2026-fall/math110/handouts/2026-08-31-sets-fields-subspaces/vector-explorer.html'
root=Path(mkdtemp(prefix='math110-week01-visual-'))
errors=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-crash-reporter'])
    page=browser.new_page(viewport={'width':1500,'height':1100},device_scale_factor=1,offline=True)
    page.on('pageerror',lambda e:errors.append(str(e)))
    # Managed Chromium blocks file:// navigation; inject the exact local file
    # while the browser context is offline. No server or remote asset is used.
    html=html_path.read_text()
    page.set_content(html,wait_until='load')
    assert page.locator('#plot').get_attribute('data-tick')=='20'
    # The first trial must invite discovery without showing the final values.
    assert page.locator('h1').inner_text()=='Find two vectors whose sum is (4, 2)'
    assert page.locator('#coordinate-equations').is_visible()
    assert not page.locator('#finished-equation').is_visible()
    assert not page.locator('#answer-known').is_visible()
    assert page.locator('#answer-unknown').is_visible()
    assert 't = 3' not in page.locator('#unique-copy').inner_text()
    assert page.locator('#plot-instructions').is_visible()
    assert page.locator('#plot #plot-instructions').count()==0
    assert 'Drag' not in page.locator('#plot').text_content()
    assert page.locator('#endpoint-label').text_content()=='possible endpoints from this u'
    for t in [1,2]:
        page.get_by_role('button',name=f't = {t}',exact=True).click()
        assert not page.locator('#finished-equation').is_visible()
        assert not page.locator('#answer-known').is_visible()
        page.screenshot(path=str(root/f'explorer-v2-trial-{t}.png'),full_page=True)
    page.get_by_role('button',name='t = 3',exact=True).click()
    assert page.locator('#finished-equation').is_visible()
    assert page.locator('#answer-known').is_visible()
    assert not page.locator('#answer-unknown').is_visible()
    page.screenshot(path=str(root/'explorer-v2-trial-3.png'),full_page=True)
    page.get_by_role('button',name='t = 1',exact=True).click()
    assert page.locator('#answer-known').is_visible() # Discovery persists.
    # A fresh viewer can also request the uniqueness argument before finding 3.
    page.close()
    page=browser.new_page(viewport={'width':1500,'height':1100},device_scale_factor=1,offline=True)
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.set_content(html,wait_until='load')
    page.locator('#show-unique').check()
    assert page.locator('#answer-known').is_visible()
    assert page.locator('#plot').get_attribute('data-tick')=='20'
    assert 'uniqueness-mode' in page.locator('#plot').get_attribute('class')
    assert '4 + 2 = 6' in page.locator('#uniqueness').text_content()
    page.screenshot(path=str(root/'explorer-v2-uniqueness-from-1.png'),full_page=True)
    page.locator('#show-unique').uncheck()
    for tick in range(81):
        page.locator('#t-slider').evaluate('(el,t)=>{el.value=t/20;el.dispatchEvent(new Event("input",{bubbles:true}));}',tick)
        assert page.locator('#plot').get_attribute('data-valid')==str(tick==60).lower()
        assert page.locator('#residual').get_attribute('x2')=='560'
        assert page.locator('#residual').get_attribute('y2')=='280'
        assert page.locator('#residual').get_attribute('stroke')==('#f4c56a' if tick==60 else '#ff7d86')
        assert abs(float(page.locator('#possible-line').get_attribute('y1'))-(205-150*tick/20))<1e-9
    for t in [1,2,3]:
        page.get_by_role('button',name=f't = {t}',exact=True).click()
        assert page.locator('#plot').get_attribute('data-tick')==str(t*20)
    page.locator('#show-unique').check()
    assert 'unique-hidden' not in page.locator('#uniqueness').get_attribute('class')
    page.screenshot(path=str(root/'explorer-v2-uniqueness.png'),full_page=True)
    page.locator('#show-unique').uncheck()
    page.locator('#handle').focus()
    page.keyboard.press('ArrowLeft')
    assert page.locator('#plot').get_attribute('data-tick')=='59'
    assert page.locator('#plot').get_attribute('data-valid')=='false'
    page.keyboard.press('ArrowRight')
    assert page.locator('#plot').get_attribute('data-valid')=='true'
    # Drag the point to t=2 with the actual on-screen coordinate transform.
    box=page.locator('#plot').bounding_box()
    def xy(x,y):return (box['x']+x*box['width']/900,box['y']+y*box['height']/660)
    page.mouse.move(*xy(485,205));page.mouse.down();page.mouse.move(*xy(410,280),steps=15);page.mouse.up()
    assert page.locator('#plot').get_attribute('data-tick')=='40'
    page.get_by_role('button',name='Next trial →',exact=True).click()
    assert page.locator('#plot').get_attribute('data-tick')=='60'
    page.locator('#play').click()
    page.wait_for_function('document.querySelector("#plot").dataset.tick === "60"',timeout=8000)
    assert page.locator('#play').inner_text()=='▶ Play trials'
    # Check narrow layout: controls remain usable, no horizontal page overflow.
    page.set_viewport_size({'width':390,'height':844})
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    page.screenshot(path=str(root/'explorer-v2-mobile.png'),full_page=True)
    assert not errors,errors
    browser.close()
print(f'Screenshots: {root}')
print('PASS: initial answer concealed; equations visible; trial-3 and uniqueness reveal; persistent reveal; instructions outside SVG; attached endpoint callout; all 81 slider positions, trial buttons, exact gold threshold, endpoint line geometry, keyboard, drag, step, play landing at t=3, uniqueness toggle, narrow viewport, no JavaScript errors.')
