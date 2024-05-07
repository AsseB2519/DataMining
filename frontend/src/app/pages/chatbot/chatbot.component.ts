import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

import { TalkService } from '../../services/talk.service';
import Talk from 'talkjs';

@Component({
  selector: 'app-chatbot',
  standalone: true,
  imports: [],
  templateUrl: './chatbot.component.html',
  styleUrl: './chatbot.component.less'
})
export class ChatbotComponent implements OnInit {

  private chatbox: Talk.Chatbox | undefined;
  private session: Talk.Session | undefined;

  @ViewChild('talkjsContainer') talkjsContainer!: ElementRef;

  constructor(private talkService: TalkService) {}

  ngOnInit() {
    this.createChatbox();
  }

  private async createChatbox() {
    const session = await this.talkService.createCurrentSession();

    this.chatbox = await this.talkService.createChatbox(session);
    this.chatbox.mount(this.talkjsContainer.nativeElement);
  }

}
