// dynamic imports are within functions so they don't happen until called
DMP_CONTEXT.loadBundle({

    "homepage/index": () => [
        import(/* webpackMode: "eager" */ "./index.js"),
        import(/* webpackMode: "eager" */ "./../styles/index.css"),
    ],

    "homepage/base_ajax": () => [
    ],

    "homepage/base": () => [
        import(/* webpackMode: "eager" */ "./../styles/base.css"),
    ],

})