<script>
     
    let {
        options = {},
        data = '',
        class: class_attr,
    } = $$restProps
    
    function init(node) {
        let off
        import('./quill.ts').then(({quill}) => {
            off = quill(node, data, {
                theme: 'snow',
                ...options,
            })
        })
        return {
            destroy() {
                off && off()
            },
        }
    }
    </script>
    
    <div {...class_attr ? {class: class_attr} : {}} class="  rounded-sm h-full overflow-y-scroll  ">
        <div
            use:init
            on:text-change
        ></div>
    </div>
    