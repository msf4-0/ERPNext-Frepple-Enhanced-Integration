frappe.pages['frepple-test-page'].on_page_load = (wrapper) => {
	const page = frappe.ui.make_app_page({
		'parent': wrapper,
		'title': 'This is frepple testing page',
		'single_column': true
	});

	new FreppleDashboard(page, wrapper);
}

class FreppleDashboard {
	constructor(page, wrapper) {
		this.currentDashboard = false;
		this.wrapper = wrapper;
		this.pageMain = $(page.main);
		this.pageTitle = $(this.wrapper).find('div.title-text');

		this.showIframe();
	}

	showIframe() {
		this.getSettings().then(
			(r) => {
				this.WEBTOKEN = r.message;

				if (this.WEBTOKEN) {					
					// prepare html
					const iFrameHtml = `
						<iframe
							src="http://localhost:5000?webtoken=${this.WEBTOKEN}"
							width="100%"
							height="750"
							marginwidth="0"
							marginheight="0"
							frameborder="no"
							scrolling="yes"
						/>
					`;

					// append html to page
					this.iFrame = $(iFrameHtml).appendTo(this.pageMain);
				}
			}
		);
	}

	getSettings() {
		return frappe.call({
			'method': 'frepple.frepple.doctype.frepple_test_page.frepple_test_page.get_iframe_url'
		});
	}
}
