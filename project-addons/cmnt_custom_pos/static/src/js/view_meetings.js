function openerp_custom_view_meetings(instance, module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

    module.ViewMeetingScreenWidget = module.ScreenWidget.extend({
        template: 'ViewMeetingScreenWidget',

        show_leftpane: false,
        previous_screen: 'products',

        renderElement: function(){
            var self = this;
            this._super();

            // Funcionality of back button
            this.$('.back').click(function(){
                self.pos_widget.screen_selector.set_current_screen(self.previous_screen);
            });
        },

    });

    module.PosWidget.include({
        build_widgets: function(){
            var self = this;
            this._super();

            // Add View Meetings Buttom
            var view_meeting = $(QWeb.render('ViewMettingButton'));
            view_meeting.appendTo(this.$('.control-buttons'));
            this.$('.control-buttons').removeClass('oe_hidden');

            // Add Meetings Screen
            this.view_meeting_screen = new module.ViewMeetingScreenWidget(this, {});
            this.view_meeting_screen.appendTo(this.$('.screens'));
            this.screen_selector.add_screen('view_meeting', this.view_meeting_screen);

            // Link screen to click in Button
            view_meeting.click(function(){
                self.pos_widget.screen_selector.set_current_screen('view_meeting');
            });
            
        },
    });
}
