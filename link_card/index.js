/**
 * 获取网页的 open graph 信息
 */
const axios = require("axios");
const cheerio = require("cheerio");
const ogMetas = [
	"og:site_name",
	"og:description",
	"og:type",
	"og:title",
	"og:url",
	"og:image",
];
axios
	.get("https://zhuanlan.zhihu.com/p/34553961")
	.then((res) => {
		if (res.data) {
			const $ = cheerio.load(res.data);
			const metaList = $("head").find("meta");
			metaList.map((index, meta) => {
				if (ogMetas.includes(meta.attribs.property)) {
					console.log(meta.attribs.content);
				}
			});
		}
	})
	.catch((err) => {
		console.log(err);
	});
