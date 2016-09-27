function openerp_custom_view_meetings(instance, module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

   

    module.PosWidget.include({
        build_widgets: function(){
            var self = this;
            this._super();

            // if(this.pos.config.iface_splitbill){
            //     this.splitbill_screen = new module.SplitbillScreenWidget(this,{});
            //     this.splitbill_screen.appendTo(this.$('.screens'));
            //     this.screen_selector.add_screen('splitbill',this.splitbill_screen);

            //     var splitbill = $(QWeb.render('SplitbillButton'));

            //     splitbill.click(function(){
            //         if(self.pos.get('selectedOrder').get('orderLines').models.length > 0){
            //             self.pos_widget.screen_selector.set_current_screen('splitbill');
            //         }
            //     });
                
            //     splitbill.appendTo(this.$('.control-buttons'));
            //     this.$('.control-buttons').removeClass('oe_hidden');
            // }
            var view_meeting = $(QWeb.render('ViewMettingButton'));
            view_meeting.appendTo(this.$('.control-buttons'));
            this.$('.control-buttons').removeClass('oe_hidden');
            
        },
    });
}
